# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/278?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/278
- Title: Providing for consideration of the bill (H.R. 185) to advance responsible policies.
- Congress: 119
- Bill type: HRES
- Bill number: 278
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-05-13T14:18:57Z
- Update date including text: 2025-05-13T14:18:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-05-06 - Discharge: Motion to Discharge Committee filed by Mr. Boyle (PA). Petition No: 119-3. (<a href="https://clerk.house.gov/DischargePetition/2025050603">Discharge petition</a> text with signatures.)
- Latest action: 2025-03-31: Submitted in House

## Actions

- 2025-03-31 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-05-06 - Discharge: Motion to Discharge Committee filed by Mr. Boyle (PA). Petition No: 119-3. (<a href="https://clerk.house.gov/DischargePetition/2025050603">Discharge petition</a> text with signatures.)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/278",
    "number": "278",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
    "type": "HRES",
    "updateDate": "2025-05-13T14:18:57Z",
    "updateDateIncludingText": "2025-05-13T14:18:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H17000",
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Boyle (PA). Petition No: 119-3. (<a href=\"https://clerk.house.gov/DischargePetition/2025050603\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-03-31T16:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres278ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 278\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. McGovern submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 185) to advance responsible policies.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 185) to advance responsible policies. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 4 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Rules or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 185.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 185 no later than one week after passage.\n#### 4.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is as follows:\nStrike all after the enacting clause and insert the following: 1. In general Section 310 of the Congressional Budget Act of 1974 ( 2 U.S.C. 641 ) is amended by adding at the end the following: \u2018 \u201c(h) Limitation on cuts to certain programs Notwithstanding any other provision of law, it shall not be in order in the Senate or the House of Representatives to consider any reconciliation bill or reconciliation resolution reported pursuant to a concurrent resolution on the budget agreed to under section 301 or 304, or a joint resolution pursuant to section 258C of the Balanced Budget and Emergency Deficit Control Act of 1985, or any amendment thereto or conference report thereon that\u2014 \u2018 \u201c(1) reduces enrollment or benefits for individuals enrolled in the Medicaid program under title XIX of the Social Security Act; or \u2018 \u201c(2) reduces eligibility or benefits for households that participate in the supplemental nutrition assistance program under the Food and Nutrition Act of 2008. \u2018 \u201c(i) Expiration of limitation on cuts to certain programs Subsection (h) shall expire on January 20, 2029. . 2. Conforming amendment Section 313(b)(1) of the Congressional Budget Act of 1974 ( 2 U.S.C. 644 ) is amended by striking the period at the end and inserting or, until January 20, 2029, if it violates section 310(h). . . .",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2753",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hands Off Medicaid and SNAP Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-12T19:11:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hres278",
          "measure-number": "278",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres278v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides for House consideration and amendment of H.R. 185.</p><p>The resolution provides for the adoption of a substitute amendment that establishes a budget point of order against considering budget reconciliation legislation in the House or the Senate that (1) reduces enrollment or benefits for individuals enrolled in the Medicaid program, or (2) reduces eligibility or benefits for households that participate in the Supplemental Nutrition Assistance Program (SNAP).</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p><p>The point of order expires on January 20, 2029.\u00a0</p>"
        },
        "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres278.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides for House consideration and amendment of H.R. 185.</p><p>The resolution provides for the adoption of a substitute amendment that establishes a budget point of order against considering budget reconciliation legislation in the House or the Senate that (1) reduces enrollment or benefits for individuals enrolled in the Medicaid program, or (2) reduces eligibility or benefits for households that participate in the Supplemental Nutrition Assistance Program (SNAP).</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p><p>The point of order expires on January 20, 2029.\u00a0</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hres278"
    },
    "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies."
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides for House consideration and amendment of H.R. 185.</p><p>The resolution provides for the adoption of a substitute amendment that establishes a budget point of order against considering budget reconciliation legislation in the House or the Senate that (1) reduces enrollment or benefits for individuals enrolled in the Medicaid program, or (2) reduces eligibility or benefits for households that participate in the Supplemental Nutrition Assistance Program (SNAP).</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p><p>The point of order expires on January 20, 2029.\u00a0</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hres278"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres278ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:19:06Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T08:06:45Z"
    }
  ]
}
```
