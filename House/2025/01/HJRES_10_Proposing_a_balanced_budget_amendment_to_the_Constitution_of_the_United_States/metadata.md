# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/10?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/10
- Title: Proposing a balanced budget amendment to the Constitution of the United States.
- Congress: 119
- Bill type: HJRES
- Bill number: 10
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-02-27T23:41:17Z
- Update date including text: 2026-02-27T23:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/10",
    "number": "10",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
    "type": "HJRES",
    "updateDate": "2026-02-27T23:41:17Z",
    "updateDateIncludingText": "2026-02-27T23:41:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:19:30Z",
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
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
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
      "sponsorshipDate": "2025-01-03",
      "state": "OH"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MT"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AR"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "KS"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IN"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "WI"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "KS"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NE"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "KY"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
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
      "sponsorshipDate": "2025-07-15",
      "state": "KS"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WI"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres10ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 10\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Nunn of Iowa (for himself, Mr. Allen , Mr. Latta , Mr. Zinke , Mr. Hill of Arkansas , Mr. Estes , Mrs. Houchin , Mr. Grothman , Mr. Mann , Mr. Calvert , and Mr. Bacon ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing a balanced budget amendment to the Constitution of the United States.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. Total outlays for any fiscal year shall not exceed total receipts for that fiscal year, unless three-fifths of the whole number of each House of Congress shall provide by law for a specific excess of outlays over receipts by a rollcall vote. 2. The limit on the debt of the United States held by the public shall not be increased, unless three-fifths of the whole number of each House shall provide by law for such an increase by a rollcall vote. 3. Prior to each fiscal year, the President shall transmit to the Congress a proposed budget for the United States Government for that fiscal year in which total outlays do not exceed total receipts. 4. No bill to increase revenue shall become law unless approved by a majority of the whole number of each House by a rollcall vote. 5. The Congress may waive the provisions of this article for any fiscal year in which a declaration of war is in effect. The provisions of this article may be waived for any fiscal year in which the United States is engaged in military conflict which causes an imminent and serious military threat to national security and is so declared by a joint resolution, adopted by a majority of the whole number of each House, which becomes law. Any such waiver must identify and be limited to the specific excess or increase for that fiscal year made necessary by the identified military conflict. 6. The Congress shall enforce and implement this article by appropriate legislation, which may rely on estimates of outlays and receipts. 7. Total receipts shall include all receipts of the United States Government except those derived from borrowing. Total outlays shall include all outlays of the United States Government except for those for repayment of debt principal. 8. This article shall take effect beginning with the fifth fiscal year beginning after its ratification. .",
      "versionDate": "2025-01-03",
      "versionType": "IH"
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "11",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified.",
      "type": "HJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "17",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "type": "HJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "type": "HJRES"
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
            "name": "Budget deficits and national debt",
            "updateDate": "2025-01-15T18:37:43Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:37:43Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2025-01-15T18:37:43Z"
          },
          {
            "name": "Income tax rates",
            "updateDate": "2025-01-15T18:37:43Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:37:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-14T16:17:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hjres10",
          "measure-number": "10",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres10v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a three-fifths roll call vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing.</p> <p>The amendment requires a three-fifths roll call vote of each chamber to increase the public debt limit. It prohibits a bill to increase revenue from becoming law unless it has been approved by a majority roll call vote of each chamber. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts.</p> <p>Congress may waive these requirements due to a declaration of war or a military conflict that causes an imminent and serious military threat to national security. </p>"
        },
        "title": "Proposing a balanced budget amendment to the Constitution of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres10.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a three-fifths roll call vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing.</p> <p>The amendment requires a three-fifths roll call vote of each chamber to increase the public debt limit. It prohibits a bill to increase revenue from becoming law unless it has been approved by a majority roll call vote of each chamber. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts.</p> <p>Congress may waive these requirements due to a declaration of war or a military conflict that causes an imminent and serious military threat to national security. </p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres10"
    },
    "title": "Proposing a balanced budget amendment to the Constitution of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a three-fifths roll call vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing.</p> <p>The amendment requires a three-fifths roll call vote of each chamber to increase the public debt limit. It prohibits a bill to increase revenue from becoming law unless it has been approved by a majority roll call vote of each chamber. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts.</p> <p>Congress may waive these requirements due to a declaration of war or a military conflict that causes an imminent and serious military threat to national security. </p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres10"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres10ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:26Z"
    }
  ]
}
```
