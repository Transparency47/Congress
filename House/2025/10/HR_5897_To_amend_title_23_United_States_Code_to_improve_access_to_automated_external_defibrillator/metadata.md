# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5897?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5897
- Title: Public Access to Defibrillation in Transportation Facilities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5897
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-01-07T09:05:50Z
- Update date including text: 2026-01-07T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5897",
    "number": "5897",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Public Access to Defibrillation in Transportation Facilities Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:50Z",
    "updateDateIncludingText": "2026-01-07T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-01",
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
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-01T17:04:22Z",
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
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5897ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5897\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Van Drew (for himself and Ms. Gillen ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to improve access to automated external defibrillators at interstate transportation facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Access to Defibrillation in Transportation Facilities Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nSudden cardiac arrest (in this section referred to as SCA ) is a leading cause of death in the United States, with an estimated 356,000 out-of-hospital cardiac arrests occurring annually.\n**(2)**\nAutomated external defibrillators (in this section referred to as AEDs ) are a vital tool in responding to SCA, as they are capable of delivering a life-saving shock to restore the heart\u2019s natural rhythm.\n**(3)**\nThere is a need for quick response times in cases of SCA, as every minute that passes without defibrillation decreases the likelihood of survival by 7 to 10 percent.\n##### (b) Sense of Congress\nIt is the sense of Congress that Federal agencies, States, and municipalities should accelerate efforts to deploy AEDs in locations that are frequented by large crowds.\n#### 3. Expansion of surface transportation block grant program to fund AED deployment\n##### (a) In general\nSection 133(b) of title 23, United States Code, is amended by adding at the end the following:\n(25) Projects to purchase and deploy automated external defibrillators for use at transportation facilities otherwise eligible for assistance under this section. (26) Projects to develop and implement written emergency action plans for responding to medical emergencies at transportation facilities otherwise eligible for assistance under this section, including the use of automated external defibrillators. .\n##### (b) Technical assistance\nThe Secretary of Transportation, in consultation with the Secretary of Health and Human Services and the Director of the Centers for Disease Control and Prevention, shall provide technical assistance to States and local officials in developing the written emergency action plans referred to in section 133(b)(26) of title 23, United States Code (as added by subsection (a) of this section).\n#### 4. Deployment of AEDS in interstate transportation facilities\n##### (a) In general\nThe Secretary of Transportation, in consultation with the Secretary of Health and Human Services, shall issue\u2014\n**(1)**\nrecommendations for the deployment of automated external defibrillators (in this section referred to as AEDs ) at interstate transportation facilities based on best practices for the placement and maintenance of AEDs; and\n**(2)**\nguidelines to assist any owner or operator of an interstate transportation facility in developing and implementing for such facility a written emergency action plan for responding to medical emergencies, including the use of AEDs.\n##### (b) Technical assistance\nThe Secretary of Transportation shall provide technical assistance to owners and operators of interstate transportation facilities in complying with the recommendations and guidelines issued under subsection (a).\n##### (c) Enforcement\nIn carrying out financial assistance programs of the Department of Transportation, including its components, the Secretary of Transportation may impose such additional terms and conditions as the Secretary determines necessary to provide for adoption of the recommendations and guidelines issued under subsection (a).\n##### (d) Definitions\nIn this section:\n**(1) Interstate System**\nThe term Interstate System has the meaning given such term in section 101 of title 23, United States Code.\n**(2) Interstate transportation facility**\nThe term interstate transportation facility includes\u2014\n**(A)**\na bus terminal, a ferry terminal, and a rail passenger transportation terminal;\n**(B)**\na highway rest area on the Interstate System;\n**(C)**\na vehicle used to provide rail passenger transportation, other than a vehicle used exclusively to provide transportation between station stops located within 15 minutes of each other (as determined using times established in public timetables); and\n**(D)**\nsuch other facilities as the Secretary of Transportation determines appropriate.\n**(3) Rail passenger transportation**\nThe term rail passenger transportation includes transportation provided by a rail fixed guideway public transportation system, an intercity passenger rail system, or a commuter rail passenger transportation system that receives Federal assistance, as identified by the Secretary of Transportation.\n#### 5. Effective date\nThis Act, and the amendments made by this Act, shall apply beginning on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-10-31",
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
        "updateDate": "2025-11-19T14:24:08Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5897ih.xml"
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
      "title": "Public Access to Defibrillation in Transportation Facilities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Access to Defibrillation in Transportation Facilities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to improve access to automated external defibrillators at interstate transportation facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:15Z"
    }
  ]
}
```
