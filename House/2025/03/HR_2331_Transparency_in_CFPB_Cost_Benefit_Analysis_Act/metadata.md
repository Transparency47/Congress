# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2331?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2331
- Title: Transparency in CFPB Cost-Benefit Analysis Act
- Congress: 119
- Bill type: HR
- Bill number: 2331
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-01-30T21:16:27Z
- Update date including text: 2026-01-30T21:16:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2331",
    "number": "2331",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Transparency in CFPB Cost-Benefit Analysis Act",
    "type": "HR",
    "updateDate": "2026-01-30T21:16:27Z",
    "updateDateIncludingText": "2026-01-30T21:16:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "KY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2331ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2331\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Loudermilk (for himself and Mr. Barr ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo enhance rulemaking requirements for the Bureau of Consumer Financial Protection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency in CFPB Cost-Benefit Analysis Act .\n#### 2. Transparency in cost-benefit analysis\nSection 1022(b) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5512(b) ) is amended by adding at the end the following:\n(5) Additional rulemaking requirements (A) In general Each notice of proposed rulemaking issued by the Bureau shall be published in its entirety in the Federal Register and shall include\u2014 (i) a statement of the need for the proposed regulation; (ii) an examination of why the Bureau must undertake the proposed regulation and why the private market, State, local, or tribal authorities cannot adequately address the problem; (iii) an examination of whether the proposed regulation is duplicative, inconsistent, or incompatible with other Federal regulations and orders; (iv) if the proposed regulation is found to be duplicative, inconsistent, or incompatible with other Federal regulations and orders, a discussion of\u2014 (I) why the proposed regulation is justified; (II) how the proposed regulation can coexist with the existing regulations; and (III) how the Bureau plans to reduce the regulatory burden associated with the duplicative, inconsistent, or incompatible proposed regulation; (v) a quantitative and qualitative assessment of all anticipated direct and indirect costs and benefits of the proposed regulation, including\u2014 (I) compliance costs for all regulated entities, including small businesses; (II) effects on economic activity, efficiency, competition and capital formation; (III) regulatory and administrative costs of implementation; and (IV) costs imposed on State, local and tribal entities; (vi) an identification of reasonable alternatives to the regulation, including modification of an existing regulation; (vii) an analysis of the costs and benefits, both quantitative and qualitative, of any alternative identified pursuant to clause (v); (viii) if the Bureau determines the proposed regulation would increase costs for small businesses, then the Bureau shall consult the Office of Advocacy within the Small Business Administration to determine ways to minimize the effect of direct and indirect costs imposed on small businesses by the proposed regulation; (ix) if quantified net benefits of the proposed action do not outweigh the quantified net benefits of the alternatives, a justification of the regulation; (x) if quantified benefits identified pursuant to clause (iv) do not outweigh the quantified costs of the regulation, a justification of the regulation; (xi) an assessment of how the burden imposed by the regulation will be distributed; including whether consumers, or small businesses will be disproportionately burdened; and (xii) when feasible, and using appropriate statistical techniques, a probability distribution of the relevant outcomes of the proposed regulation. (B) Assumptions and studies used With respect to the information required to be included under subparagraph (A), the Bureau will include\u2014 (i) a discussion of underlying assumptions used as a basis for such information; and (ii) a description of any studies or data used in preparing such information, and whether such studies were peer-reviewed. .",
      "versionDate": "2025-03-25",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-04-04T16:35:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119hr2331",
          "measure-number": "2331",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-25",
          "originChamber": "HOUSE",
          "update-date": "2026-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2331v00",
            "update-date": "2026-01-30"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Transparency in CFPB Cost-Benefit Analysis Act </strong></p> <p>This bill sets forth information required to be included in a rulemaking made by the Consumer Financial Protection Bureau (CFPB). Specifically, the CFPB must publish a justification of the proposed rulemaking; a quantitative and qualitative assessment of all anticipated direct and indirect costs and benefits; alternatives to the proposed rulemaking; impacts on small businesses; and any assumptions, data, or studies used in preparing this information. </p>"
        },
        "title": "Transparency in CFPB Cost-Benefit Analysis Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2331.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Transparency in CFPB Cost-Benefit Analysis Act </strong></p> <p>This bill sets forth information required to be included in a rulemaking made by the Consumer Financial Protection Bureau (CFPB). Specifically, the CFPB must publish a justification of the proposed rulemaking; a quantitative and qualitative assessment of all anticipated direct and indirect costs and benefits; alternatives to the proposed rulemaking; impacts on small businesses; and any assumptions, data, or studies used in preparing this information. </p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119hr2331"
    },
    "title": "Transparency in CFPB Cost-Benefit Analysis Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Transparency in CFPB Cost-Benefit Analysis Act </strong></p> <p>This bill sets forth information required to be included in a rulemaking made by the Consumer Financial Protection Bureau (CFPB). Specifically, the CFPB must publish a justification of the proposed rulemaking; a quantitative and qualitative assessment of all anticipated direct and indirect costs and benefits; alternatives to the proposed rulemaking; impacts on small businesses; and any assumptions, data, or studies used in preparing this information. </p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119hr2331"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2331ih.xml"
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
      "title": "Transparency in CFPB Cost-Benefit Analysis Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency in CFPB Cost-Benefit Analysis Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance rulemaking requirements for the Bureau of Consumer Financial Protection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:44Z"
    }
  ]
}
```
