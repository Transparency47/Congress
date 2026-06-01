# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3081
- Title: Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3081
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2026-04-03T19:59:36Z
- Update date including text: 2026-04-03T19:59:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3081",
    "number": "3081",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025",
    "type": "S",
    "updateDate": "2026-04-03T19:59:36Z",
    "updateDateIncludingText": "2026-04-03T19:59:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T17:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3081is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3081\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Cruz (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to provide for reciprocal marketing approval of certain drugs, biological products, and devices that are authorized to be lawfully marketed abroad, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025 .\n#### 2. Reciprocal marketing approval for certain drugs, biological products, and devices\nThe Federal Food, Drug, and Cosmetic Act is amended by inserting after section 524B of such Act ( 21 U.S.C. 360n\u20132 ) the following:\n524C. Reciprocal marketing approval (a) In general A covered product with reciprocal marketing approval in effect under this section is deemed to be subject to an application or premarket notification for which an approval or clearance is in effect under section 505(c), 510(k), or 515 of this Act or section 351(a) of the Public Health Service Act, as applicable. (b) Eligibility The Secretary shall, with respect to a covered product, grant reciprocal marketing approval if\u2014 (1) the sponsor of the covered product submits a request for reciprocal marketing approval; and (2) the request demonstrates to the Secretary\u2019s satisfaction that\u2014 (A) the covered product is authorized to be lawfully marketed in one or more of the countries included in the list under section 802(b)(1) or in the United Kingdom; (B) absent reciprocal marketing approval, the covered product is not approved or cleared for marketing, as described in subsection (a); (C) the Secretary has not, because of any concern relating to the safety or effectiveness of the covered product, rescinded or withdrawn any such approval or clearance; (D) the authorization to market the covered product in one or more of the countries included in the list under section 802(b)(1) or in the United Kingdom has not, because of any concern relating to the safety or effectiveness of the covered product, been rescinded or withdrawn; (E) the covered product is not a banned device under section 516; and (F) there is a public health or unmet medical need for the covered product in the United States. (c) Safety and effectiveness (1) In general The Secretary\u2014 (A) may decline to grant reciprocal marketing approval under this section with respect to a covered product if the Secretary affirmatively determines that the covered product\u2014 (i) is a drug that is not safe and effective; or (ii) is a device for which there is no reasonable assurance of safety and effectiveness; and (B) may condition reciprocal marketing approval under this section on the conduct of specified postmarket studies, which may include such studies pursuant to a risk evaluation and mitigation strategy under section 505\u20131. (2) Report to Congress Upon declining to grant reciprocal marketing approval under this section with respect to a covered product, the Secretary shall\u2014 (A) include the denial in a list of such denials for each month; and (B) not later than the end of the respective month, submit the list to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate. (d) Request A request for reciprocal marketing approval shall\u2014 (1) be in such form, be submitted in such manner, and contain such information as the Secretary deems necessary to determine whether the criteria listed in subsection (b)(2) are met; and (2) include, with respect to each country included in the list under section 802(b)(1) where the covered product is authorized to be lawfully marketed, as described in subsection (b)(2)(A), an English translation of the dossier issued by such country to authorize such marketing. (e) Timing The Secretary shall issue an order granting, or declining to grant, reciprocal marketing approval with respect to a covered product not later than 30 days after the Secretary\u2019s receipt of a request under subsection (b)(1) for the product. An order issued under this subsection shall take effect subject to Congressional disapproval under subsection (g). (f) Labeling; device classification During the 30-day period described in subsection (e)\u2014 (1) the Secretary and the sponsor of the covered product shall expeditiously negotiate and finalize the form and content of the labeling for a covered product for which reciprocal marketing approval is to be granted; and (2) in the case of a device for which reciprocal marketing approval is to be granted, the Secretary shall\u2014 (A) classify the device pursuant to section 513; and (B) determine whether, absent reciprocal marketing approval, the device would need to be cleared pursuant to section 510(k) or approved pursuant to section 515 to be lawfully marketed under this Act. (g) Congressional disapproval of FDA orders (1) In general A decision of the Secretary to decline to grant reciprocal marketing approval under this section shall not take effect if a joint resolution of disapproval of the decision is enacted. (2) Procedure (A) In general Subject to subparagraph (B), the procedures described in subsections (b) through (g) of section 802 of title 5, United States Code, shall apply to the consideration of a joint resolution under this subsection. (B) Terms For purposes of this subsection\u2014 (i) the reference to section 801(a)(1) in section 802(b)(2)(A) of title 5, United States Code, shall be considered to refer to subsection (c)(2); and (ii) the reference to section 801(a)(1)(A) in section 802(e)(2) of title 5, United States Code, shall be considered to refer to subsection (c)(2). (3) Effect of Congressional disapproval Reciprocal marketing approval under this section with respect to the applicable covered product shall take effect upon enactment of a joint resolution of disapproval under this subsection. (h) Applicability of relevant provisions The provisions of this Act shall apply with respect to a covered product for which reciprocal marketing approval is in effect to the same extent and in the same manner as such provisions apply with respect to a product for which approval or clearance of an application or premarket notification under section 505(c), 510(k), or 515 of this Act or section 351(a) of the Public Health Service Act, as applicable, is in effect. (i) Fees for request For purposes of imposing fees under chapter VII, a request for reciprocal marketing approval under this section shall be treated as an application or premarket notification for approval or clearance under section 505(c), 510(k), or 515 of this Act or section 351(a) of the Public Health Service Act, as applicable. (j) Outreach The Secretary shall conduct an outreach campaign to encourage the sponsors of covered products that are potentially eligible for reciprocal marketing approval to request such approval. (k) Covered product defined In this section, the term covered product means a drug, biological product, or device. .",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-02-26",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1632",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025",
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
        "updateDate": "2025-11-25T20:30:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-30",
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
          "measure-id": "id119s3081",
          "measure-number": "3081",
          "measure-type": "s",
          "orig-publish-date": "2025-10-30",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3081v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-10-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of </strong><strong>2025</strong></p><p>This bill establishes a reciprocal marketing approval process that allows for the sale of a drug, biological product, or medical device that has not been approved by the Food and Drug Administration (FDA) if the product is approved for sale in another country and there is an unmet need for the product.</p><p>Specifically, in order to receive reciprocal approval, the bill requires the product's sponsor to demonstrate, among other things, that (1) the product has been approved in one of the countries specified in the bill, (2) neither the FDA nor any of the specified countries have withdrawn approval for the product because of safety or effectiveness concerns, and (3) there is a public health or unmet medical need for the product.</p><p>The FDA may decline approval if it determines that the product is not safe or effective. The FDA may condition reciprocal approval on the conduct of postmarket studies.</p><p>The FDA must issue a decision on whether to grant a request for reciprocal marketing approval within 30 days of receiving the request.</p><p>Congress may pass a joint resolution to grant reciprocal marketing approval of a product that the FDA declines to approve through the reciprocal process.</p>"
        },
        "title": "Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3081.xml",
    "summary": {
      "actionDate": "2025-10-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of </strong><strong>2025</strong></p><p>This bill establishes a reciprocal marketing approval process that allows for the sale of a drug, biological product, or medical device that has not been approved by the Food and Drug Administration (FDA) if the product is approved for sale in another country and there is an unmet need for the product.</p><p>Specifically, in order to receive reciprocal approval, the bill requires the product's sponsor to demonstrate, among other things, that (1) the product has been approved in one of the countries specified in the bill, (2) neither the FDA nor any of the specified countries have withdrawn approval for the product because of safety or effectiveness concerns, and (3) there is a public health or unmet medical need for the product.</p><p>The FDA may decline approval if it determines that the product is not safe or effective. The FDA may condition reciprocal approval on the conduct of postmarket studies.</p><p>The FDA must issue a decision on whether to grant a request for reciprocal marketing approval within 30 days of receiving the request.</p><p>Congress may pass a joint resolution to grant reciprocal marketing approval of a product that the FDA declines to approve through the reciprocal process.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s3081"
    },
    "title": "Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of </strong><strong>2025</strong></p><p>This bill establishes a reciprocal marketing approval process that allows for the sale of a drug, biological product, or medical device that has not been approved by the Food and Drug Administration (FDA) if the product is approved for sale in another country and there is an unmet need for the product.</p><p>Specifically, in order to receive reciprocal approval, the bill requires the product's sponsor to demonstrate, among other things, that (1) the product has been approved in one of the countries specified in the bill, (2) neither the FDA nor any of the specified countries have withdrawn approval for the product because of safety or effectiveness concerns, and (3) there is a public health or unmet medical need for the product.</p><p>The FDA may decline approval if it determines that the product is not safe or effective. The FDA may condition reciprocal approval on the conduct of postmarket studies.</p><p>The FDA must issue a decision on whether to grant a request for reciprocal marketing approval within 30 days of receiving the request.</p><p>Congress may pass a joint resolution to grant reciprocal marketing approval of a product that the FDA declines to approve through the reciprocal process.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s3081"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3081is.xml"
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
      "title": "Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reciprocity Ensures Streamlined Use of Lifesaving Treatments Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to provide for reciprocal marketing approval of certain drugs, biological products, and devices that are authorized to be lawfully marketed abroad, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:18Z"
    }
  ]
}
```
