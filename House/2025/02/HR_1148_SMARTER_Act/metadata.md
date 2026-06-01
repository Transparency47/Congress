# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1148
- Title: SMARTER Act
- Congress: 119
- Bill type: HR
- Bill number: 1148
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-03-02T15:23:49Z
- Update date including text: 2026-03-02T15:23:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1148",
    "number": "1148",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "SMARTER Act",
    "type": "HR",
    "updateDate": "2026-03-02T15:23:49Z",
    "updateDateIncludingText": "2026-03-02T15:23:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1148ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1148\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to require States to consider prohibiting cost recovery related to smart grid projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Misappropriating Ratepayer Tariffs for Excessive Resources Act or the SMARTER Act .\n#### 2. Smart grid cost recovery\n##### (a) Consideration and determination respecting certain ratemaking standards\n**(1) Repeal**\nSection 111(d)(18)(B) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d)(18)(B) ) is repealed.\n**(2) Establishment**\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Prohibition on rate recovery for smart grid investments No electric utility may recover from ratepayers any capital, operating expenditure, or other costs of the electric utility relating to the deployment of any smart grid system. .\n##### (b) Obligations To consider and determine\n**(1) Time limitations**\nSection 112(b) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622(b) ) is amended by adding at the end the following:\n(8) (A) Not later than 1 year after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority) and each nonregulated utility shall commence consideration under section 111, or set a hearing date for consideration, with respect to the standard established by paragraph (22) of section 111(d). (B) Not later than 2 years after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority), and each nonregulated electric utility shall complete the consideration and make the determination under section 111 with respect to the standard established by paragraph (22) of section 111(d). .\n**(2) Failure to comply**\nSection 112(c) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622(c) ) is amended by adding at the end the following: In the case of the standard established by paragraph (22) of section 111(d), the reference contained in this subsection to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (22). .\n**(3) Prior State actions**\nSection 112 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622 ) is amended by adding at the end the following:\n(i) Prior State actions Subsections (b) and (c) shall not apply to the standard established by paragraph (22) of section 111(d) in the case of any electric utility in a State if, before the date of enactment of this subsection\u2014 (1) the State has implemented for the electric utility the standard (or a comparable standard); (2) the State regulatory authority for the State or the relevant nonregulated electric utility has conducted a proceeding to consider implementation of the standard (or a comparable standard) for the electric utility; or (3) the State legislature has voted on the implementation of the standard (or a comparable standard) for the electric utility during the 3-year period ending on that date of enactment. .\n##### (c) Prior and pending proceedings\nSection 124 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2634 ) is amended by adding at the end the following: In the case of the standard established by paragraph (22) of section 111(d), the reference contained in this section to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (22). .",
      "versionDate": "2025-02-07",
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
        "name": "Energy",
        "updateDate": "2025-03-11T18:04:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1148",
          "measure-number": "1148",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1148v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Misappropriating\u00a0Ratepayer Tariffs for Excessive Resources Act or the SMARTER Act</strong></p><p>This bill requires nonregulated utilities and state regulators of utilities to consider implementing a standard\u00a0to prohibit electric utilities from recovering costs relating to the deployment of any smart grid system from their consumers. It also repeals the current requirement for states to consider authorizing electric utilities to recover costs relating to the deployment of certain smart grid systems from their consumers.</p><p>Within a year, each nonregulated\u00a0utility and state regulatory authority must consider adopting the prohibition. Within two years, they must determine whether or not to implement the prohibition. However, the deadlines do not apply if a state has already considered or implemented a comparable standard.</p>"
        },
        "title": "SMARTER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1148.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Misappropriating\u00a0Ratepayer Tariffs for Excessive Resources Act or the SMARTER Act</strong></p><p>This bill requires nonregulated utilities and state regulators of utilities to consider implementing a standard\u00a0to prohibit electric utilities from recovering costs relating to the deployment of any smart grid system from their consumers. It also repeals the current requirement for states to consider authorizing electric utilities to recover costs relating to the deployment of certain smart grid systems from their consumers.</p><p>Within a year, each nonregulated\u00a0utility and state regulatory authority must consider adopting the prohibition. Within two years, they must determine whether or not to implement the prohibition. However, the deadlines do not apply if a state has already considered or implemented a comparable standard.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119hr1148"
    },
    "title": "SMARTER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Misappropriating\u00a0Ratepayer Tariffs for Excessive Resources Act or the SMARTER Act</strong></p><p>This bill requires nonregulated utilities and state regulators of utilities to consider implementing a standard\u00a0to prohibit electric utilities from recovering costs relating to the deployment of any smart grid system from their consumers. It also repeals the current requirement for states to consider authorizing electric utilities to recover costs relating to the deployment of certain smart grid systems from their consumers.</p><p>Within a year, each nonregulated\u00a0utility and state regulatory authority must consider adopting the prohibition. Within two years, they must determine whether or not to implement the prohibition. However, the deadlines do not apply if a state has already considered or implemented a comparable standard.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119hr1148"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1148ih.xml"
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
      "title": "SMARTER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SMARTER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Misappropriating Ratepayer Tariffs for Excessive Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to require States to consider prohibiting cost recovery related to smart grid projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:27Z"
    }
  ]
}
```
