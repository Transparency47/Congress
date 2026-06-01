# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1384
- Title: Abortion Funding Awareness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1384
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-04-30T11:03:19Z
- Update date including text: 2026-04-30T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1384",
    "number": "1384",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Abortion Funding Awareness Act of 2025",
    "type": "S",
    "updateDate": "2026-04-30T11:03:19Z",
    "updateDateIncludingText": "2026-04-30T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
        "item": [
          {
            "date": "2025-04-09T19:39:56Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-09T19:39:56Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "TN"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "AL"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "IN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "ID"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "TX"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1384is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1384\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Banks (for himself, Mrs. Blackburn , Mr. Tuberville , Mr. Young , Mr. Budd , Mr. Daines , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require States to report information on Medicaid payments to abortion providers.\n#### 1. Short title\nThis Act may be cited as the Abortion Funding Awareness Act of 2025 .\n#### 2. Required reporting of Medicaid payments to abortion providers\n##### (a) In general\nNot later than 60 days after the end of the first fiscal year ending after the date of enactment of this Act and each fiscal year thereafter, each State that makes a Medicaid payment from Federal funds during the fiscal year for any items or services furnished by an abortion provider shall\u2014\n**(1)**\nsubmit to the Secretary a report on all such payments; and\n**(2)**\npublish the report on a public internet website of the State.\n##### (b) Report described\nThe report under subsection (a) shall, with respect to a State that makes a Medicaid payment from Federal funds during the fiscal year for any items or services furnished by an abortion provider, include the following:\n**(1)**\nWith respect to each such payment, each of the following:\n**(A)**\nA specification of the amount of the payment.\n**(B)**\nA specification of the purposes for which the payment was made.\n**(C)**\nA comparison of the amount of the payment with the amount of any such payment to the provider involved in any prior fiscal year.\n**(2)**\nA specification of the number of abortions performed during the fiscal year by the provider involved and the gestational age with respect to each such abortion.\n**(3)**\nA specification of the method of abortion used.\n##### (c) Report to Congress\nNot later than 90 days after the end of each fiscal year described in subsection (a), the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and to the Committee on Finance of the Senate, and publish on a public internet website of the Department of Health and Human Services, a report that\u2014\n**(1)**\ncontains the State reports submitted pursuant to subsection (a) for the fiscal year; and\n**(2)**\nincludes a summary of the reports.\n##### (d) Definitions\nIn this section:\n**(1) Abortion**\nThe term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device\u2014\n**(A)**\nto intentionally kill the unborn child of a woman known to be pregnant; or\n**(B)**\nto intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014\n**(i)**\nafter viability, to produce a live birth and preserve the life and health of the child born alive; or\n**(ii)**\nto remove a dead unborn child.\n**(2) Abortion provider**\nThe term abortion provider means an entity that\u2014\n**(A)**\nperforms (or refers an individual for) an abortion; or\n**(B)**\ncontrols, is controlled by, or is under common control with, an entity described in subparagraph (A).\n**(3) Medicaid payment from Federal funds**\nThe term Medicaid payment from Federal funds means a payment for which there is Federal financial participation under title XIX of the Social Security Act.\n**(4) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(5) State**\nThe term State has the meaning given the term for purposes of title XIX of the Social Security Act.\n##### (e) Conforming amendments to Social Security Act\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended\u2014\n**(1)**\nin paragraph (86), by striking and after the semicolon;\n**(2)**\nin paragraph (87)(D), by striking the period and inserting ; and ; and\n**(3)**\nby inserting after paragraph (87) the following:\n(88) provide for the submission of reports in accordance with section 2 of the Abortion Funding Awareness Act of 2025 . .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2779",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Abortion Funding Awareness Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-05-19T16:15:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119s1384",
          "measure-number": "1384",
          "measure-type": "s",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1384v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Abortion Funding Awareness Act of 2025</strong></p><p>This bill establishes reporting requirements for states regarding certain Medicaid payments to abortion providers.</p><p>Specifically, the bill requires states that make Medicaid payments using\u00a0federal funds for any items or services furnished by an abortion provider to annually (1) submit a report to the Centers for Medicare & Medicaid Services on all such payments, and (2) publish the report on the state's website. The report must include specified information, including the number of abortions performed by the providers and the gestational age with respect to each such abortion. (Current law restricts the use of federal funds for abortions to cases of rape, incest, or life endangerment of the woman. States may use their own funds to cover abortions in other cases.)</p>"
        },
        "title": "Abortion Funding Awareness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1384.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Abortion Funding Awareness Act of 2025</strong></p><p>This bill establishes reporting requirements for states regarding certain Medicaid payments to abortion providers.</p><p>Specifically, the bill requires states that make Medicaid payments using\u00a0federal funds for any items or services furnished by an abortion provider to annually (1) submit a report to the Centers for Medicare & Medicaid Services on all such payments, and (2) publish the report on the state's website. The report must include specified information, including the number of abortions performed by the providers and the gestational age with respect to each such abortion. (Current law restricts the use of federal funds for abortions to cases of rape, incest, or life endangerment of the woman. States may use their own funds to cover abortions in other cases.)</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s1384"
    },
    "title": "Abortion Funding Awareness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Abortion Funding Awareness Act of 2025</strong></p><p>This bill establishes reporting requirements for states regarding certain Medicaid payments to abortion providers.</p><p>Specifically, the bill requires states that make Medicaid payments using\u00a0federal funds for any items or services furnished by an abortion provider to annually (1) submit a report to the Centers for Medicare & Medicaid Services on all such payments, and (2) publish the report on the state's website. The report must include specified information, including the number of abortions performed by the providers and the gestational age with respect to each such abortion. (Current law restricts the use of federal funds for abortions to cases of rape, incest, or life endangerment of the woman. States may use their own funds to cover abortions in other cases.)</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s1384"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1384is.xml"
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
      "title": "Abortion Funding Awareness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Abortion Funding Awareness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require States to report information on Medicaid payments to abortion providers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:18Z"
    }
  ]
}
```
