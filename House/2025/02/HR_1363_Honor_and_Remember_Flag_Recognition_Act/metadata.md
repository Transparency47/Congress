# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1363
- Title: Honor and Remember Flag Recognition Act
- Congress: 119
- Bill type: HR
- Bill number: 1363
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-05-13T08:06:46Z
- Update date including text: 2026-05-13T08:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1363",
    "number": "1363",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Honor and Remember Flag Recognition Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:46Z",
    "updateDateIncludingText": "2026-05-13T08:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:34:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "PA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "IA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NJ"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "NC"
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
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "VA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AL"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "KS"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "AL"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
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
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CO"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NJ"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1363ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1363\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Davis of North Carolina (for himself, Mr. Thompson of Pennsylvania , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 36, United States Code, to designate the Honor and Remember Flag created by Honor and Remember, Inc., as an official symbol to recognize and honor members of the Armed Forces who died in the line of duty, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honor and Remember Flag Recognition Act .\n#### 2. Designation of Honor and Remember flag for fallen members of the Armed Forces\n##### (a) Findings\nCongress finds the following:\n**(1)**\nSince the Revolutionary War, more than one million members of the United States Armed Forces have paid the ultimate price by sacrificing their lives in the line of duty.\n**(2)**\nThe contributions of those fallen members of the Armed Forces are deserving of national recognition.\n**(3)**\nCurrently, there is no officially recognized symbol that acknowledges members of the Armed Forces who died in the line of duty.\n##### (b) Designation\nChapter 9 of title 36, United States Code, is amended by adding at the end the following new section:\n904. Honor and Remember Flag for fallen members of the Armed Forces (a) Designation The Honor and Remember Flag created by Honor and Remember, Inc., is designated as the symbol of our Nation\u2019s concern and commitment to honoring and remembering the lives of all members of the United States Armed Forces who have lost their lives in the line of duty. (b) Required Display (1) The Honor and Remember Flag shall be displayed at the locations specified in subsection (c) on the days specified in paragraph (2). (2) The required Honor and Remember Flag display days are the following: (A) Armed Forces Day, the third Saturday in May. (B) Memorial Day, the last Monday in May. (C) Flag Day, June 14. (D) Independence Day, July 4. (E) National POW/MIA Recognition Day. (F) Veterans Day, November 11. (3) In addition to the days specified in paragraph (2), Honor and Remember Flag display days include\u2014 (A) in the case of display at the World War II Memorial, Korean War Veterans Memorial, and Vietnam Veterans Memorial (required by subsection (c)(3)), any day on which the flag of the United States is displayed; (B) in the case of display at medical centers of the Department of Veterans Affairs (required by subsection (c)(7)), any day on which the flag of the United States is displayed; and (C) in the case of display at United States Postal Service post offices (required by subsection (c)(8)), the last business day before a day specified in paragraph (2) that in any year is not itself a business day. (c) Locations for Flag Display The locations for the display of the Honor and Remember Flag under subsection (b) are the following: (1) The Capitol. (2) The White House. (3) The World War II Memorial, the Korean War Veterans Memorial, and the Vietnam Veterans Memorial. (4) Each national cemetery. (5) The buildings containing the official office of\u2014 (A) the Secretary of State; (B) the Secretary of Defense; (C) the Secretary of Veterans Affairs; and (D) the Director of the Selective Service System. (6) Each major military installation, as designated by the Secretary of Defense. (7) Each medical center of the Department of Veterans Affairs. (8) Each United States Postal Service post office. (d) Display To Be in a Manner Visible to the Public Display of the Honor and Remember Flag pursuant to this section shall be in a manner designed to ensure visibility to the public. (e) Limitation This section may not be construed or applied so as to require any employee to report to work solely for the purpose of providing for the display of the Honor and Remember Flag or any other flag. .\n##### (c) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding at the end the following new item:\n904. Honor and Remember Flag for fallen members of the Armed Forces. .\n##### (d) Regulations for implementation\nNot later than 180 days after the date of the enactment of this Act, the head of each department, agency, or other establishment responsible for a location specified in subsection (c) of section 904 of title 36, United States Code, as added by subsection (a), shall prescribe such regulations as necessary to carry out such section.\n##### (e) Procurement and distribution of flags\nNot later than 30 days after the date of the enactment of this Act, the Administrator of General Services shall commence the procurement of Honor and Remember Flags and distribute them as necessary to permit compliance with section 904 of title 36, United States Code, as added by subsection (a).",
      "versionDate": "2025-02-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-07-08T12:58:32Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-07-08T12:58:32Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-07-08T12:58:32Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2025-07-08T12:58:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T12:43:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1363",
          "measure-number": "1363",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1363v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Honor and Remember Flag Recognition Act</b></p> <p>This bill designates the Honor and Remember Flag, created by Honor and Remember, Inc., as a national symbol to honor service members who died in the line of duty and specifies federal locations and dates for its display.</p>"
        },
        "title": "Honor and Remember Flag Recognition Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1363.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Honor and Remember Flag Recognition Act</b></p> <p>This bill designates the Honor and Remember Flag, created by Honor and Remember, Inc., as a national symbol to honor service members who died in the line of duty and specifies federal locations and dates for its display.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119hr1363"
    },
    "title": "Honor and Remember Flag Recognition Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Honor and Remember Flag Recognition Act</b></p> <p>This bill designates the Honor and Remember Flag, created by Honor and Remember, Inc., as a national symbol to honor service members who died in the line of duty and specifies federal locations and dates for its display.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119hr1363"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1363ih.xml"
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
      "title": "Honor and Remember Flag Recognition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honor and Remember Flag Recognition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 36, United States Code, to designate the Honor and Remember Flag created by Honor and Remember, Inc., as an official symbol to recognize and honor members of the Armed Forces who died in the line of duty, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:18Z"
    }
  ]
}
```
