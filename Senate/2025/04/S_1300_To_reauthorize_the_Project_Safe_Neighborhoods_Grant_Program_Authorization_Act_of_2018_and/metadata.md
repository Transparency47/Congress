# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1300
- Title: Project Safe Neighborhoods Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1300
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2025-12-05T21:50:01Z
- Update date including text: 2025-12-05T21:50:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1300",
    "number": "1300",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:50:01Z",
    "updateDateIncludingText": "2025-12-05T21:50:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-03T23:21:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MI"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "IA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NE"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "MO"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "sponsorshipWithdrawnDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1300is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1300\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Cornyn (for himself, Mr. Peters , Mr. Grassley , Mr. Tillis , Mrs. Fischer , Mr. Hawley , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo reauthorize the Project Safe Neighborhoods Grant Program Authorization Act of 2018, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Project Safe Neighborhoods Reauthorization Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nLaunched in 2001, the Project Safe Neighborhoods program is a nationwide initiative that brings together Federal, State, local, and Tribal law enforcement officials, prosecutors, community leaders, and other stakeholders to identify the most pressing crime problems in a community and work collaboratively to address those problems.\n**(2)**\nThe Project Safe Neighborhoods program\u2014\n**(A)**\noperates in all 94 Federal judicial districts throughout the 50 States and territories of the United States; and\n**(B)**\nimplements 4 key components to successfully reduce violent crime in communities, including community engagement, prevention and intervention, focused and strategic enforcement, and accountability.\n#### 3. Reauthorization\n##### (a) Definitions\nSection 2 of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60701 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), and (3) as paragraphs (2), (4), and (5), respectively;\n**(2)**\nby inserting before paragraph (2), as so redesignated, the following:\n(1) the term crime analyst means an individual employed by a law enforcement agency for the purpose of separating information into key components and contributing to plans of action to understand, mitigate, and neutralize criminal threats; ; and\n**(3)**\nby inserting after paragraph (2), as so redesignated, the following:\n(3) the term law enforcement assistant means an individual employed by a law enforcement agency or a prosecuting agency for the purpose of aiding law enforcement officers in investigative or administrative duties; .\n##### (b) Use of funds\nSection 4(b) of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60703(b) ) is amended\u2014\n**(1)**\nin paragraph (3), by striking or at the end;\n**(2)**\nin paragraph (4), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(5) hiring crime analysts to assist with violent crime reduction efforts; (6) the cost of overtime for law enforcement officers, prosecutors, and law enforcement assistants that assist with the Program; and (7) purchasing, implementing, and using technology to assist with violent crime reduction efforts. .\n##### (c) Authorization of appropriations\nSection 6 of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60705 ) is amended by striking \u201cfiscal years 2019 through 2021\u201d and inserting fiscal years 2026 through 2030 .\n#### 4. Task force support\n##### (a) Short title\nThis section may be cited as the Officer Ella Grace French and Sergeant Jim Smith Task Force Support Act of 2025 .\n##### (b) Amendment\nSection 4(b) of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60703(b) ), as amended by section 3(b), is amended\u2014\n**(1)**\nin paragraph (6), by striking and at the end;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) support for multi-jurisdictional task forces. .\n#### 5. Transparency\nNot less frequently than annually, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that details, for each area in which the Project Safe Neighborhoods Block Grant Program operates and with respect to the 1-year period preceding the date of the report\u2014\n**(1)**\nhow the area spent funds under the Project Safe Neighborhoods Block Grant Program;\n**(2)**\nthe community outreach efforts performed in the area; and\n**(3)**\nthe number and a description of the violent crime offenses committed in the area, including murder, non-negligent manslaughter, rape, robbery, and aggravated assault.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1726",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Community life and organization",
            "updateDate": "2025-09-02T19:14:05Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T19:14:05Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-09-02T19:14:05Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-09-02T19:14:05Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-09-02T19:14:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-05T13:08:27Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1300is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Officer Ella Grace French and Sergeant Jim Smith Task Force Support Act of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Project Safe Neighborhoods Grant Program Authorization Act of 2018, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:31Z"
    }
  ]
}
```
