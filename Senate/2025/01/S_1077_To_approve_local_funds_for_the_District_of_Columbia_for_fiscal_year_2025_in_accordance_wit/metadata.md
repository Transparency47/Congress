# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1077?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1077
- Title: District of Columbia Local Funds Act, 2025
- Congress: 119
- Bill type: S
- Bill number: 1077
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2025-10-09T03:26:20Z
- Update date including text: 2025-10-09T03:26:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - Floor: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Voice Vote. (consideration: CR S1772-1773; text: CR S1772-1773)
- 2025-03-14 - Floor: Passed/agreed to in Senate: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Voice Vote.
- 2025-03-17 - Floor: Message on Senate action sent to the House.
- 2025-03-18 12:03:36 - Floor: Received in the House.
- 2025-03-18 12:03:50 - Floor: Held at the desk.
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - Floor: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Voice Vote. (consideration: CR S1772-1773; text: CR S1772-1773)
- 2025-03-14 - Floor: Passed/agreed to in Senate: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Voice Vote.
- 2025-03-17 - Floor: Message on Senate action sent to the House.
- 2025-03-18 12:03:36 - Floor: Received in the House.
- 2025-03-18 12:03:50 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1077",
    "number": "1077",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "District of Columbia Local Funds Act, 2025",
    "type": "S",
    "updateDate": "2025-10-09T03:26:20Z",
    "updateDateIncludingText": "2025-10-09T03:26:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-03-18",
      "actionTime": "12:03:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-03-18",
      "actionTime": "12:03:36",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Voice Vote. (consideration: CR S1772-1773; text: CR S1772-1773)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Introduced in the Senate, read twice, considered, read the third time, and passed without amendment by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MD"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MD"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "WA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1077cps.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1077\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Ms. Collins (for herself, Mr. Van Hollen , Ms. Alsobrooks , Mrs. Murray , Mr. Warner , Mr. Kaine , and Mr. Kim ) introduced the following bill; which was considered, read the third time, and passed\nA BILL\nTo approve local funds for the District of Columbia for fiscal year 2025, in accordance with the Fiscal Year 2025 Local Budget Act of 2024, and to establish provisions for the use of such funds.\n#### 1. Short title\nThis Act may be cited as the District of Columbia Local Funds Act, 2025 .\n#### 2. District of Columbia Local Funds\nLocal funds are appropriated for the District of Columbia for the current fiscal year out of the General Fund of the District of Columbia ( General Fund ) for programs and activities set forth in the Fiscal Year 2025 Local Budget Act of 2024 (D.C. Law 25\u2013218) and at rates set forth under such Act, as amended as of the date of enactment of this Act: Provided, That notwithstanding any other provision of law, except as provided in section 450A of the District of Columbia Home Rule Act (section 1\u2013204.50a, D.C. Official Code), sections 816 and 817 of the Financial Services and General Government Appropriations Act, 2009 (secs. 47\u2013369.01 and 47\u2013369.02, D.C. Official Code), and provisions of this Act, the total amount appropriated in this Act for operating expenses for the District of Columbia for fiscal year 2025 by this section shall not exceed the estimates included in the Fiscal Year 2025 Local Budget Act of 2024, as amended as of the date of enactment of this Act or the sum of the total revenues of the District of Columbia for such fiscal year: Provided further, That the amount appropriated may be increased by proceeds of one-time transactions, which are expended for emergency or unanticipated operating or capital needs: Provided further, That such increases shall be approved by enactment of local District law and shall comply with all reserve requirements contained in the District of Columbia Home Rule Act: Provided further, That the Chief Financial Officer of the District of Columbia shall take such steps as are necessary to assure that the District of Columbia meets these requirements, including the apportioning by the Chief Financial Officer of the appropriations and funds made available to the District during fiscal year 2025, except that the Chief Financial Officer may not reprogram for operating expenses any funds derived from bonds, notes, or other obligations issued for capital projects.",
      "versionDate": "2025-03-14",
      "versionType": "Considered and Passed Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1077es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1077\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo approve local funds for the District of Columbia for fiscal year 2025, in accordance with the Fiscal Year 2025 Local Budget Act of 2024, and to establish provisions for the use of such funds.\n#### 1. Short title\nThis Act may be cited as the District of Columbia Local Funds Act, 2025 .\n#### 2. District of Columbia Local Funds\nLocal funds are appropriated for the District of Columbia for the current fiscal year out of the General Fund of the District of Columbia ( General Fund ) for programs and activities set forth in the Fiscal Year 2025 Local Budget Act of 2024 (D.C. Law 25\u2013218) and at rates set forth under such Act, as amended as of the date of enactment of this Act: Provided, That notwithstanding any other provision of law, except as provided in section 450A of the District of Columbia Home Rule Act (section 1\u2013204.50a, D.C. Official Code), sections 816 and 817 of the Financial Services and General Government Appropriations Act, 2009 (secs. 47\u2013369.01 and 47\u2013369.02, D.C. Official Code), and provisions of this Act, the total amount appropriated in this Act for operating expenses for the District of Columbia for fiscal year 2025 by this section shall not exceed the estimates included in the Fiscal Year 2025 Local Budget Act of 2024, as amended as of the date of enactment of this Act or the sum of the total revenues of the District of Columbia for such fiscal year: Provided further, That the amount appropriated may be increased by proceeds of one-time transactions, which are expended for emergency or unanticipated operating or capital needs: Provided further, That such increases shall be approved by enactment of local District law and shall comply with all reserve requirements contained in the District of Columbia Home Rule Act: Provided further, That the Chief Financial Officer of the District of Columbia shall take such steps as are necessary to assure that the District of Columbia meets these requirements, including the apportioning by the Chief Financial Officer of the appropriations and funds made available to the District during fiscal year 2025, except that the Chief Financial Officer may not reprogram for operating expenses any funds derived from bonds, notes, or other obligations issued for capital projects.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "District of Columbia",
            "updateDate": "2025-04-01T15:33:22Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-04-01T15:33:36Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-04-01T15:33:26Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-01T15:33:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-03-31T16:53:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
    "originChamber": "Senate",
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
          "measure-id": "id119s1077",
          "measure-number": "1077",
          "measure-type": "s",
          "orig-publish-date": "2025-03-14",
          "originChamber": "SENATE",
          "update-date": "2025-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1077v00",
            "update-date": "2025-04-09"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>District of Columbia Local Funds Act, 2025</strong></p><p>This bill appropriates FY2025 local funds to the District of Columbia for programs and activities included in the District's Fiscal Year 2025 Local Budget Act of 2024.\u00a0</p><p>Under current law, Congress is required to approve the District's annual budget. This bill approves the budget and allows the District to spend local funds for programs and activities that are included in the budget at the rates specified in the budget.\u00a0</p>"
        },
        "title": "District of Columbia Local Funds Act, 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1077.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>District of Columbia Local Funds Act, 2025</strong></p><p>This bill appropriates FY2025 local funds to the District of Columbia for programs and activities included in the District's Fiscal Year 2025 Local Budget Act of 2024.\u00a0</p><p>Under current law, Congress is required to approve the District's annual budget. This bill approves the budget and allows the District to spend local funds for programs and activities that are included in the budget at the rates specified in the budget.\u00a0</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119s1077"
    },
    "title": "District of Columbia Local Funds Act, 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>District of Columbia Local Funds Act, 2025</strong></p><p>This bill appropriates FY2025 local funds to the District of Columbia for programs and activities included in the District's Fiscal Year 2025 Local Budget Act of 2024.\u00a0</p><p>Under current law, Congress is required to approve the District's annual budget. This bill approves the budget and allows the District to spend local funds for programs and activities that are included in the budget at the rates specified in the budget.\u00a0</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119s1077"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1077cps.xml"
        }
      ],
      "type": "Considered and Passed Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1077es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "District of Columbia Local Funds Act, 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T11:03:22Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "District of Columbia Local Funds Act, 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-03-15T11:08:21Z"
    },
    {
      "title": "A bill to approve local funds for the District of Columbia for fiscal year 2025, in accordance with the Fiscal Year 2025 Local Budget Act of 2024, and to establish provisions for the use of such funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T10:56:19Z"
    }
  ]
}
```
