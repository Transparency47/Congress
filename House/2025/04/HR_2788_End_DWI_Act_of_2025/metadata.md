# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2788?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2788
- Title: End DWI Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2788
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-10-29T08:05:45Z
- Update date including text: 2025-10-29T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-09 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-09 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2788",
    "number": "2788",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000871",
        "district": "1",
        "firstName": "Tracey",
        "fullName": "Rep. Mann, Tracey [R-KS-1]",
        "lastName": "Mann",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "End DWI Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-29T08:05:45Z",
    "updateDateIncludingText": "2025-10-29T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-04-09T16:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-09T21:18:22Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "HI"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "IL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "TN"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NV"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2788ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2788\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Mann (for himself, Mr. Pappas , Mr. Smith of New Jersey , and Mr. Raskin ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to provide for a national standard to prevent driving while intoxicated by requiring ignition interlocks for DWI offenders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Driving While Intoxicated Act of 2025 or the End DWI Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to Mothers Against Drunk Driving, there has been a historic increase in alcohol-impaired driving fatalities since 2019 resulting in one person dying in a driving while intoxicated crash in the United States every 39 minutes.\n**(2)**\nAccording to the National Highway Traffic Safety Administration, between 2020 and 2021, driving while intoxicated deaths increased 14 percent and 13,384 people were killed, a level not seen since 2006.\n**(3)**\nStudies show that ignition interlocks reduce recidivism, by up to 70 percent, among first-time, repeat and high-risk driving while intoxicated offenders while they are installed.\n**(4)**\nIgnition interlocks are required for people who have been convicted for driving while intoxicated in 31 States and the District of Columbia, according to the National Conference of State Legislators.\n**(5)**\nThe rise in polysubstance impaired driving significantly increases the crash risk on our nation\u2019s roads.\n**(6)**\nOne 2018 study from Washington State revealed that polysubstance impairment was the most common type of impairment found among drivers involved in fatal crashes between 2008 and 2016 and among drivers involved in fatal crashes during this timeframe, 44 percent tested positive for 2 or more substances with alcohol and THC being the most common combination.\n#### 3. National standard for ignition interlocks for DWI offenders\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. National standard for ignition interlocks for DWI offenders (a) Withholding of apportionments for non-Compliance (1) Fiscal year 2027 The Secretary shall withhold 3 percent of the amount required to be apportioned to any State under each of paragraphs (1) and (2) of section 104(b) on October 1, 2026, if the State does not meet the requirements of paragraph (3) on such date. (2) Subsequent fiscal years The Secretary shall withhold 5 percent of the amount required to be apportioned to any State under each of paragraphs (1) and (2) of section 104(b) on October 1, 2027, and on October 1 of each fiscal year thereafter, if the State does not meet the requirements of paragraph (3) on such date. (3) Requirements (A) In general A State meets the requirements of this paragraph if the State has enacted and is enforcing a law mandating a restriction on driving privileges for a driving while intoxicated offender that limits the individual to operating only motor vehicles with an ignition interlock device installed, unless a special exception applies (as determined by the respective State), for a minimum period of 180 days and remain without a violation for a minimum period (as determined by the respective State) that precedes the date of the removal of the restriction. (B) Interlock period The interlock period described in subparagraph (A) may be served by the individual during an administrative license suspension period, post-conviction, or a combination of both, as determined by the respective State. (b) Period of availability; effect of compliance and non-Compliance (1) Period of availability of withheld funds (A) Funds withheld on or before September 30, 2028 Any funds withheld under subsection (a) from apportionment to any State on or before September 30, 2028, shall remain available until the end of the third fiscal year following the fiscal year for which the funds are authorized to be appropriated. (B) Funds withheld after September 30, 2028 No funds withheld under this section from apportionment to any State after September 30, 2028, shall be available for apportionment to the State. (2) Apportionment of withheld funds after compliance If, before the last day of the period for which funds withheld under subsection (a) from apportionment are to remain available for apportionment to a State under paragraph (1)(A), the State meets the requirements of subsection (a)(3), the Secretary shall, on the first day on which the State meets the requirements, apportion to the State the funds withheld under subsection (a) that remain available for apportionment to the State. (3) Period of availability of subsequently apportioned funds (A) In general Any funds apportioned under paragraph (2) shall remain available for obligation until the end of the third fiscal year following the fiscal year in which the funds are so apportioned. (B) Treatment of certain funds Sums not obligated at the end of the period referred to in subparagraph (A) shall lapse. (4) Effect of non-compliance If, at the end of the period for which funds withheld under subsection (a) from apportionment are available for apportionment to a State under paragraph (1)(A) of this subsection, the State does not meet the requirements of subsection (a)(3), the funds shall lapse. (c) Definitions In this section: (1) Driving while intoxicated The term driving while intoxicated has the meaning given such term in section 164 and section 405. (2) Ignition interlock The term ignition interlock has the meaning given the term ignition interlock system in section 1275.3 of title 23, Code of Federal Regulations. (3) Motor vehicle The term motor vehicle has the meaning given such term in section 32101 of title 49. (4) Special exception The term special exception has the meaning defined by a State in law or regulation with respect to an ignition interlock device that may include that the individual is required to operate an employer\u2019s motor vehicle in the course and scope of employment and the business entity that owns the vehicle is not owned by the individual. (5) Violation The term violation has the meaning defined by a State in law or regulation with respect to an ignition interlock device that may include failing a breath test, failing to take or pass a re-test, circumventing an ignition interlock, tampering with an ignition interlock, or a combinations of the actions described in this paragraph. .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by inserting after the item relating to section 179 the following:\n180. National standard for ignition interlocks for DWI offenders. .\n##### (c) Conforming amendments\n**(1) Minimum penalties for repeat offenders**\nSection 164(a)(6) of title 23, United States Code, is amended by striking or controlled .\n**(2) National priority safety programs**\nSection 405(d)(6) of title 23, United States Code, is amended\u2014\n**(A)**\nin subparagraph (A)(ii) by striking registered, owned, or leased for operation and inserting operated ; and\n**(B)**\nin subparagraph (F)(i) by striking or controlled .",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-12T13:11:07Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2788ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "End DWI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-07T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End DWI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Driving While Intoxicated Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to provide for a national standard to prevent driving while intoxicated by requiring ignition interlocks for DWI offenders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:33:27Z"
    }
  ]
}
```
