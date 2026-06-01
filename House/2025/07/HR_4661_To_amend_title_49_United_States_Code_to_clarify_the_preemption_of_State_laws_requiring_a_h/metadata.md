# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4661
- Title: AMERICA DRIVES Act
- Congress: 119
- Bill type: HR
- Bill number: 4661
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-16T09:05:37Z
- Update date including text: 2025-12-16T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4661",
    "number": "4661",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000480",
        "district": "20",
        "firstName": "Vince",
        "fullName": "Rep. Fong, Vince [R-CA-20]",
        "lastName": "Fong",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "AMERICA DRIVES Act",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:37Z",
    "updateDateIncludingText": "2025-12-16T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:16:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T21:28:07Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4661ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4661\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Fong introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to clarify the preemption of State laws requiring a human occupant in an automated driving systems-equipped commercial motor vehicle, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Autonomous Mobility Ensuring Regulation, Innovation, Commerce, and Advancement Driving Reliability in Vehicle Efficiency and Safety Act or the AMERICA DRIVES Act .\n#### 2. Preemption of State laws requiring a human occupant in an automated driving systems-equipped commercial motor vehicle\n##### (a) ADS-Equipped commercial motor vehicle operation\n**(1) In general**\nSubchapter III of chapter 311 of title 49, United States Code, is amended by inserting after section 31139 the following:\n31140. ADS-equipped commercial motor vehicle operation (a) In general A commercial motor vehicle equipped with a Level 4 or Level 5 ADS may be operated in interstate commerce without\u2014 (1) a human driver on board such vehicle; or (2) a remote human driver. (b) Regulations The Secretary of Transportation shall issue regulations as necessary to implement this section. (c) Statutory construction Nothing in this subsection shall be construed to require a commercial motor vehicle to be equipped with an ADS. .\n**(2) Clerical amendment**\nThe analysis for chapter 311 of title 49, United States Code, is amended by inserting after section 31139 the following:\n31140. ADS-equipped commercial motor vehicle operation. .\n##### (b) Definitions\nSection 31132 of title 49, United States Code, is amended by adding at the end the following:\n(12) ADS-equipped vehicle means a motor vehicle equipped with an automated driving system. (13) Automated driving system or ADS means\u2014 (A) hardware and software that are collectively capable of performing the entire dynamic driving task on a sustained basis, regardless of whether such hardware or software is limited to a specific operational design domain; (B) includes only systems that meet the definition of automation levels 3, 4, or 5 under SAE International\u2019s J3016 recommended practice titled Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles , or subsequent editions of J3016 adopted by the Secretary; and (C) does not include systems that provide only assistance to a human driver. (14) Level 4 has the meaning of that term as provided in the April 2021 edition of SAE International\u2019s J3016 recommended practice titled Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles , or subsequent editions of J3016 adopted by the Secretary and refers to an ADS that is capable of providing full driving automation under defined conditions with no need for human intervention. (15) Level 5 has the meaning of that term as provided in the April 2021 edition of SAE International\u2019s J3016 recommended practice titled Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles , or subsequent editions of J3016 adopted by the Secretary and refers to an ADS that is capable of providing full driving automation under all conditions with no need for human intervention. .\n#### 3. Reducing regulatory obstacles to safe integration of automated driving systems-equipped commercial motor vehicles\n##### (a) Streamlining regulations\nNot later than September 30, 2027, the Secretary of Transportation shall address the applicability of sections 350 through 399 of title 49, Code of Federal Regulations to ADS-equipped commercial motor vehicles based on the advance notice of proposed rulemaking published on May 28, 2019 (84 Fed. Reg. 24449) that\u2014\n**(1)**\namends such sections to provide for the integration of automated driving systems into commercial vehicle operations, including updating any such sections that reasonably apply only to a human driver to clarify such regulations do not apply to an ADS or to an ADS-equipped vehicles operating with an ADS engaged and without a human driver on board, including hours of service, drug testing, electronic logging devices, commercial driver\u2019s license, and physical qualification requirements; and\n**(2)**\ndefine the terms remote driver and remote assistance as follows:\n**(A)**\nThe term remote driver means a driver who is not seated in a position to manually exercise in-vehicle braking, accelerating, steering, and transmission gear selection input devices (if any), but is able to operate the vehicle.\n**(B)**\nThe term remote assistance means event-driven provision, by a remotely located human, of information or advice to an AD2202S-equipped vehicle in driverless operation in order to facilitate trip continuation when the automated driving system encounters a situation where remote assistance could provide clarity.\n##### (b) Ensuring regulatory parity for commercial motor vehicles\nThe Secretary may not issue a regulation that unduly burdens motor carriers operating ADS-equipped vehicles or discriminates against an ADS-equipped vehicle relative to other commercial motor vehicles.\n##### (c) Ensuring regulatory flexibility for safety technologies\nSection 31113 of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (c), (d), and (e) as subsections (d), (e), and (f), respectively; and\n**(2)**\nby inserting the following after subsection (b):\n(c) Exclusion of automated driving technologies and equipment Width calculated under this section does not include automated driving system technologies or equipment. .\n##### (d) Definitions\nThe terms defined in section 31132 of title 49, United States Code, apply to this section.\n#### 4. Regulatory interpretations\nSections 392.22 and 393.95(f) of title 49, Code of Federal Regulations, and any related regulations shall be applied as if to include cab-mounted warning beacons as a permissible warning device, as proposed by the Exemption Application published on March 3, 2023 (88 Fed. Reg. 14665, Docket No. FMCSA\u20132023\u20130071).",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-16T17:17:47Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4661ih.xml"
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
      "title": "AMERICA DRIVES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AMERICA DRIVES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Autonomous Mobility Ensuring Regulation, Innovation, Commerce, and Advancement Driving Reliability in Vehicle Efficiency and Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to clarify the preemption of State laws requiring a human occupant in an automated driving systems-equipped commercial motor vehicle, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:30Z"
    }
  ]
}
```
