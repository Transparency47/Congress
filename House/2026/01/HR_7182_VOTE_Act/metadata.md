# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7182
- Title: VOTE Act
- Congress: 119
- Bill type: HR
- Bill number: 7182
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-05-19T08:05:42Z
- Update date including text: 2026-05-19T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by Voice Vote.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7182",
    "number": "7182",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "VOTE Act",
    "type": "HR",
    "updateDate": "2026-05-19T08:05:42Z",
    "updateDateIncludingText": "2026-05-19T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
        "item": [
          {
            "date": "2026-05-14T17:20:50Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-21T15:02:30Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "GA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7182ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7182\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Ms. Johnson of Texas (for herself, Mr. Morelle , Ms. Norton , Mr. Johnson of Georgia , and Mr. Casten ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to establish minimum notification requirements for voters affected by polling place changes.\n#### 1. Short title\nThis Act may be cited as the Voter Outreach for Transparent Elections Act or the VOTE Act .\n#### 2. Minimum notification requirements for voters affected by polling place changes\n##### (a) Requirements\nSection 302 of the Help America Vote Act of 2002 ( 52 U.S.C. 21082 ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following new subsection:\n(d) Minimum notification requirements for voters affected by polling place changes (1) In general If a State assigns an individual who is a registered voter in a State to a polling place with respect to an election for Federal office which is not the same polling place to which the individual was previously assigned with respect to the most recent election for Federal office in the State in which the individual was eligible to vote\u2014 (A) the State shall notify the individual of the location of the polling place not later than 7 days before the date of the election; (B) the appropriate election official of the State shall post a general notice on the website of the State or jurisdiction, on social media platforms (if available), and on signs at the prior polling place; and (C) if the State makes such an assignment fewer than 7 days before the date of the election and the individual appears on the date of the election at the polling place to which the individual was previously assigned, the State shall make every reasonable effort to enable the individual to vote on the date of the election. (2) Methods of notification The appropriate election official shall notify an individual under paragraph (1)(A) by mail, telephone, and (if available) text message and electronic mail. (3) Requirements for vote centers In the case of a jurisdiction in which individuals are not assigned to specific polling places, not later than 2 days before the beginning of an early voting period, the appropriate election official shall notify each individual eligible to vote in such jurisdiction of the location of all polling places at which the individual may vote. (4) Notice with respect to closed polling places (A) In general If a location which served as a polling place for an election for Federal office in a State does not serve as a polling place in the next election for Federal office held in the State, the State shall ensure that signs are posted at such location on the date of the election and during any early voting period for the election containing the following information: (i) A statement that the location is not serving as a polling place in the election. (ii) The locations serving as polling places in the election in the jurisdiction involved. (iii) The name and address of any substitute polling place serving the same precinct and directions from the former polling place to the new polling place. (iv) Contact information, including a telephone number and website, for the appropriate State or local election official through which an individual may find the polling place to which the individual is assigned for the election. (B) Internet posting Each State which is required to post signs under subparagraph (A) shall also provide such information through a website and through social media (if available). (C) Linguistic preference The notices required under this subsection shall comply with the requirements of section 203 of the Voting Rights Act of 1965 ( 52 U.S.C. 10503 ). (5) Effective date This subsection shall apply with respect to elections held on or after January 1, 2026. .\n##### (b) Conforming amendment\nSection 302(e) of such Act ( 52 U.S.C. 21082(f) ), as redesignated by subsection (a), is amended by striking Each State and inserting Except as provided in subsection (d)(5), each State .",
      "versionDate": "2026-01-21",
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
        "updateDate": "2026-02-11T13:46:16Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7182ih.xml"
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
      "title": "VOTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T11:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VOTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T11:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Voter Outreach for Transparent Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T11:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to establish minimum notification requirements for voters affected by polling place changes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T11:33:24Z"
    }
  ]
}
```
