# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2666?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2666
- Title: CBO Scoring Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 2666
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-06-30T13:41:54Z
- Update date including text: 2025-06-30T13:41:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2666",
    "number": "2666",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "CBO Scoring Accountability Act",
    "type": "HR",
    "updateDate": "2025-06-30T13:41:54Z",
    "updateDateIncludingText": "2025-06-30T13:41:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MO"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NC"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "VA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "WI"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "AR"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TN"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "VA"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "MN"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2666ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2666\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Barr (for himself, Mrs. Wagner , Mr. Nehls , Mr. Evans of Colorado , Mr. Latta , Mr. Edwards , Ms. Tenney , Mr. Rose , Mr. McGuire , Mr. Rutherford , Mrs. Miller of Illinois , Mr. Mills , Mr. Hurd of Colorado , Mr. Van Orden , Mr. Westerman , Mr. McCormick , Mr. Issa , Mr. Ogles , and Mr. Collins ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to require the Congressional Budget Office to provide an analysis with respect to major legislation over time, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CBO Scoring Accountability Act .\n#### 2. Supplemental analysis with respect to major legislation\n##### (a) In general\nPart A of title IV of the Congressional Budget and Impoundment Control Act of 1974 is amended by adding at the end the following:\n407. Supplemental estimates of major legislation (a) Mandatory analysis of major legislation enacted into law Not later than annually for the first 10 years after the date of the enactment of any major legislation, the Director of the Congressional Budget Office shall prepare and make publicly available an analysis of the results of carrying out the provisions of such major legislation, which shall include\u2014 (1) an estimate of the costs and the amount of any change in Federal revenues as a result of such legislation; (2) a comparison of such costs or changes in Federal revenue against previous estimates prepared with respect to such legislation; and (3) an update to any estimates for the costs or changes in Federal revenue for such major legislation, as applicable. (b) Report to Congress With respect to an analysis prepared under subsection (a) for any major legislation, the Director shall submit to Congress a report that explains the cause of a discrepancy if there is, with respect to any provision in such legislation, any discrepancy\u2014 (1) between the actual costs provided in such analysis and such costs as provided in previous estimates for such legislation that is greater than or equal to a 10 percent difference; or (2) between the actual changes in Federal revenue provided in such analysis and such changes as provided in previous estimates for such legislation that is greater than or equal to a 10 percent difference. (c) Agency assistance Each department, agency, establishment, or regulatory agency or commission, shall provide to the Director such information and assistance as the Director may reasonably request to assist the Director in carrying out this section. (d) Major legislation defined In this section, the term major legislation means any bill or joint resolution that would be projected to result in outlays of mandatory spending or receipts of Federal revenue equal to or greater than 0.25 percent of the current projected gross domestic product of the United States for that year. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Congressional Budget and Impoundment Control Act of 1974 is amended by inserting after the item relating to section 406 the following:\nSec. 407. Supplemental estimates of major legislation. .",
      "versionDate": "2025-04-07",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-13T16:03:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2666",
          "measure-number": "2666",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2025-06-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2666v00",
            "update-date": "2025-06-30"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>CBO Scoring Accountability Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to provide additional cost\u00a0estimates and reports regarding\u00a0major legislation that has been enacted into law.</p><p>Under the bill, <em>major legislation</em> is any bill or joint resolution that would be projected to result in outlays of mandatory spending or receipts of federal revenue equal to or greater than 0.25% of the current projected gross domestic product of the United States for that year.</p><p>For the first 10 years after\u00a0major legislation has been enacted into law, the bill requires CBO to annually prepare and make publicly available an analysis of the results of carrying out the provisions of the legislation. The analysis must include</p><ul><li>an estimate of the costs and the change in federal revenue as a result of the legislation,</li><li>a comparison of the current and previous estimates of the costs and change in revenue, and</li><li>any applicable updates to the estimates.</li></ul><p>The bill also requires CBO to submit reports to Congress that explain any discrepancy between the actual and estimated costs and change in revenue that is greater than or equal to 10%.\u00a0</p>"
        },
        "title": "CBO Scoring Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2666.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>CBO Scoring Accountability Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to provide additional cost\u00a0estimates and reports regarding\u00a0major legislation that has been enacted into law.</p><p>Under the bill, <em>major legislation</em> is any bill or joint resolution that would be projected to result in outlays of mandatory spending or receipts of federal revenue equal to or greater than 0.25% of the current projected gross domestic product of the United States for that year.</p><p>For the first 10 years after\u00a0major legislation has been enacted into law, the bill requires CBO to annually prepare and make publicly available an analysis of the results of carrying out the provisions of the legislation. The analysis must include</p><ul><li>an estimate of the costs and the change in federal revenue as a result of the legislation,</li><li>a comparison of the current and previous estimates of the costs and change in revenue, and</li><li>any applicable updates to the estimates.</li></ul><p>The bill also requires CBO to submit reports to Congress that explain any discrepancy between the actual and estimated costs and change in revenue that is greater than or equal to 10%.\u00a0</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2666"
    },
    "title": "CBO Scoring Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>CBO Scoring Accountability Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to provide additional cost\u00a0estimates and reports regarding\u00a0major legislation that has been enacted into law.</p><p>Under the bill, <em>major legislation</em> is any bill or joint resolution that would be projected to result in outlays of mandatory spending or receipts of federal revenue equal to or greater than 0.25% of the current projected gross domestic product of the United States for that year.</p><p>For the first 10 years after\u00a0major legislation has been enacted into law, the bill requires CBO to annually prepare and make publicly available an analysis of the results of carrying out the provisions of the legislation. The analysis must include</p><ul><li>an estimate of the costs and the change in federal revenue as a result of the legislation,</li><li>a comparison of the current and previous estimates of the costs and change in revenue, and</li><li>any applicable updates to the estimates.</li></ul><p>The bill also requires CBO to submit reports to Congress that explain any discrepancy between the actual and estimated costs and change in revenue that is greater than or equal to 10%.\u00a0</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2666"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2666ih.xml"
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
      "title": "CBO Scoring Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CBO Scoring Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to require the Congressional Budget Office to provide an analysis with respect to major legislation over time, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T04:48:24Z"
    }
  ]
}
```
