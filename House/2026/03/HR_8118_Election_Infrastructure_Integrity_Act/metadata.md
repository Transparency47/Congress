# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8118?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8118
- Title: Election Infrastructure Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 8118
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-13T20:58:08Z
- Update date including text: 2026-04-13T20:58:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8118",
    "number": "8118",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000190",
        "district": "5",
        "firstName": "Ralph",
        "fullName": "Rep. Norman, Ralph [R-SC-5]",
        "lastName": "Norman",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Election Infrastructure Integrity Act",
    "type": "HR",
    "updateDate": "2026-04-13T20:58:08Z",
    "updateDateIncludingText": "2026-04-13T20:58:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AZ"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8118ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8118\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Norman (for himself, Mr. Moore of Alabama , and Mr. Crane ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require the Election Assistance Commission to establish and maintain a publicly accessible database of private vendors that provide, support, or maintain any component of the election systems used in the administration of elections for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Election Infrastructure Integrity Act .\n#### 2. Election vendor transparency database\n##### (a) In general\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21083 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Election vendor transparency database (a) In general The Commission shall establish and maintain a publicly accessible database of private vendors that provide, support, or maintain any component of the election systems used in the administration of elections for Federal office as submitted under subsection (b) by each State, unit of local government, and component of a State or unit of local government which is responsible for the administration of an election for Federal office. (b) Requirement To submit information to commission Each State, unit of local government, or component of a State or unit of local government which is responsible for the administration of an election for Federal office shall, not later than 30 days after the date of each election for Federal office held in such State, submit to the Commission the information required under subsection (c) with respect to each private vendor that provided, supported, or maintained any component of the election systems used in the administration of such election for Federal office and the Commission shall promptly add such information to the database established under subsection (a). (c) Information required With respect to a vendor described in subsection (b), the information required is as follows: (1) The identity of the vendor. (2) The terms of any contract or agreement with the vendor, except with respect to any information withheld due to security reasons. (3) Information with respect to the ownership of the vendor, including any parent companies, beneficial owners, and any foreign ownership or controlling interests. (d) Prohibition on federal funds for election administration If noncompliant Notwithstanding any other provision of law, no Federal funds may be provided under this Act or any other Act to administer an election for Federal office in a State if the State does not comply with the requirements under this section. (e) Definitions In this section\u2014 (1) the term beneficial owner means a person that is determined to be a beneficial owner under section 240.13d\u20133 of title 17, Code of Federal Regulations, or any successor regulation; (2) the term election system means a voting system, an election management system, a voter registration website or database, an electronic pollbook, a system for tabulating or reporting election results, an election agency communications system, or any other information system (as defined in section 3502 of title 44, United States Code) that the Commission identifies as central to the management, support, or administration of a Federal election; and (3) the term voting system has the meaning given the term in section 301(b) of the Help America Vote Act of 2002 ( 52 U.S.C. 21081(b) ). .\n##### (b) Conforming amendment relating to enforcement\nSection 401 of such Act ( 52 U.S.C. 21111 ) is amended by striking and 304 and inserting 304, and 305 .\n##### (c) Clerical amendments\nThe table of contents of such Act is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to sections 306 and 307; and\n**(2)**\nby inserting after the item relating to section 304 the following new item:\nSec. 305. Election vendor transparency database. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to elections for Federal office held in 2026 and each succeeding year.",
      "versionDate": "2026-03-26",
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
        "updateDate": "2026-04-13T20:58:08Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8118ih.xml"
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
      "title": "Election Infrastructure Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Election Infrastructure Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Election Assistance Commission to establish and maintain a publicly accessible database of private vendors that provide, support, or maintain any component of the election systems used in the administration of elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:38Z"
    }
  ]
}
```
