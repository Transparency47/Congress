# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3719?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3719
- Title: Restoring American Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 3719
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-03-20T08:07:03Z
- Update date including text: 2026-03-20T08:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3719",
    "number": "3719",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Restoring American Freedom Act",
    "type": "HR",
    "updateDate": "2026-03-20T08:07:03Z",
    "updateDateIncludingText": "2026-03-20T08:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "TN"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "IN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "FL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "MS"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "AZ"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "GA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "SC"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ID"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3719ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3719\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Huizenga (for himself, Mr. Burchett , Mr. Shreve , Mr. Self , Mrs. Luna , Mr. Guest , Mr. Hamadeh of Arizona , and Mr. Clyde ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the employees, officers, and agents of the Department of State, and persons and entities awarded grants or contracts or otherwise provided, directly or indirectly, Federal funds from the Department of State, from censoring the free speech of United States citizens.\n#### 1. Short title\nThis Act may be cited as the Restoring American Freedom Act .\n#### 2. Prohibiting censorship of free speech of United States citizens\n##### (a) Prohibiting censorship of free speech\n**(1) In general**\nSection 1(b)(3) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(b)(3) ) is amended by adding at the end the following:\n(G) monitor and ensure that\u2014 (i) no Department employee, officer, and agent, and no person or entity awarded a grant or contract or otherwise provided, directly or indirectly, Federal funds from the Department, engages in or facilitates conduct that would unconstitutionally abridge the free speech (as such term is defined in section 2(b)(2)(C) of the Restoring American Freedom Act) of a United States citizen; (ii) none of the funds authorized to be appropriated or otherwise made available to the Secretary are used to engage in or facilitate conduct that would abridge the free speech (as so defined) of a United States citizen; and (iii) appropriate action is taken to correct past misconduct by each Department employee, officer, and agent, and each person or entity awarded a grant or contract or otherwise provided, directly or indirectly, Federal funds from the Department, who engaged in or facilitated the censorship of the free speech (as so defined) of a United States citizen. .\n**(2) Clerical amendments**\nSection 1(b)(3) of such Act is amended\u2014\n**(A)**\nin subparagraph (E), by striking ; and and inserting a semicolon; and\n**(B)**\nin subparagraph (F)\u2014\n**(i)**\nin clause (iii), by striking the semicolon at the end and inserting ; and ;\n**(ii)**\nby striking clause (iv); and\n**(iii)**\nin clause (v),\n**(I)**\nby striking bureaus. and inserting bureaus; and ; and\n**(II)**\nby redesignating clause (v) as clause (iv).\n##### (b) Prohibiting using funds to censor free speech\n**(1) In general**\nNo funds authorized to be appropriated or otherwise made available to the Secretary of State may be awarded, granted, or otherwise provided, directly or indirectly, to any person or entity that\u2014\n**(A)**\npublishes or disseminates an advertising blacklist; or\n**(B)**\ncreates, tests, or distributes a censorship tool without sufficient safeguards, as determined by the Under Secretary for Public Diplomacy, for preventing such tool from being used to censor the free speech of a United States citizen.\n**(2) Definitions**\nIn this subsection:\n**(A) Advertising blacklist**\nThe term advertising blacklist means a curated list used to identify a United States citizen for the purpose of discouraging or prohibiting an advertiser from placing an advertisement with, or providing financial support to, such citizen because of the content of the free speech of such citizen.\n**(B) Censor**\nThe term censor means to scrutinize and examine the free speech of a United States citizen with the intent to suppress such free speech, and includes\u2014\n**(i)**\nexerting substantial coercive pressure on a third party, such as a social media company, to moderate, remove, or otherwise suppress such free speech; or\n**(ii)**\ncontacting, directly or indirectly, such as through an academic institution, a social media company, to moderate, remove, or otherwise suppress such protected speech.\n**(C) Free speech**\nThe term free speech means speech protected by the First Amendment of the United States Constitution from being suppressed by the United States Government.\n**(3) Enforcement**\nAs soon as practicable, but not later than 7 days after the date on which the Secretary of State is notified of each employee, officer, and agent of the Department of State, and of each person and entity awarded a grant or contract or otherwise provided, directly or indirectly, Federal funds from the Department of State, who is actually or potentially engaging in or facilitating the censorship of the free speech of a United States citizen, such Secretary shall notify the Chairman and ranking member of the Committee on Foreign Affairs in the House of Representatives, the Chairman and ranking member of the Committee on Foreign Relations in the Senate, and such United States citizen of such censorship.",
      "versionDate": "2025-06-04",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-18T12:55:43Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3719ih.xml"
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
      "title": "Restoring American Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring American Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the employees, officers, and agents of the Department of State, and persons and entities awarded grants or contracts or otherwise provided, directly or indirectly, Federal funds from the Department of State, from censoring the free speech of United States citizens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T06:48:49Z"
    }
  ]
}
```
