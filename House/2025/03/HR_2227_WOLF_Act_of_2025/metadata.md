# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2227?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2227
- Title: WOLF Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2227
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-09-03T08:05:21Z
- Update date including text: 2025-09-03T08:05:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2227",
    "number": "2227",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "WOLF Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-03T08:05:21Z",
    "updateDateIncludingText": "2025-09-03T08:05:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:07:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NM"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "AZ"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "AZ"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NM"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2227ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2227\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Stanton (for himself, Mr. Vasquez , Mr. Schweikert , and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Act of 2014 to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the WOlf and Livestock Fairness Act of 2025 or the WOLF Act of 2025 .\n#### 2. Livestock indemnity payment rates\nSection 1501(b)(2) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(b)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting appropriately;\n**(2)**\nin the matter preceding clause (i) (as so redesignated), by striking Indemnity payments and inserting the following:\n(A) In general Except as provided in subparagraph (B), indemnity payments ; and\n**(3)**\nby adding at the end the following:\n(B) Attacks by Mexican gray wolves In the case of attacks on livestock by Mexican gray wolves, indemnity payments to an eligible producer on a farm under paragraph (1) shall be made at a rate of 100 percent of the market value of the affected livestock, as determined by the Secretary, on the applicable date described in clause (i) or (ii) of subparagraph (A). .\n#### 3. Emergency relief to mitigate effect of Mexican gray wolves\nSection 1501(d) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(d) ) is amended by adding at the end the following:\n(5) Emergency relief to mitigate effect of Mexican gray wolves (A) In general Each fiscal year, the Secretary shall use funds made available under paragraph (1) to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves, as determined by the Secretary. (B) Formula Not later than 180 days after the date of enactment of this paragraph, the Secretary shall develop a formula to determine the amount of emergency relief to provide to a producer of livestock under subparagraph (A), which shall take into consideration the following factors: (i) The herd size of the producer. (ii) The average annual number of confirmed depredations by Mexican gray wolves per producer in the State in which the producer is located. (iii) The average annual increase in management costs for producers due to Mexican gray wolves during the preceding 5 years in the State in which the producer is located. (iv) The average annual decrease in birth rates of herds of producers due to Mexican gray wolves during the preceding 5 years in the State in which the producer is located. (v) The depredation prevention practices carried out by the producer, if any, as reported through the wolf compensation and prevention program established by section 6202 of the Omnibus Public Land Management Act of 2009 ( 7 U.S.C. 8351 note; Public Law 111\u201311 ). (C) Consultation In carrying out this paragraph, the Secretary shall consult with, and request information from, as necessary, the Administrator of the Farm Service Agency, the Administrator of the Animal and Plant Health Inspection Service, and the Director of the United States Fish and Wildlife Service. (D) Annual report Not later than 1 year after the date on which emergency relief is first provided under this paragraph, and annually thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report on activities carried out under this paragraph, which shall include an identification of the following: (i) The amount of emergency relief distributed to producers under this paragraph. (ii) The number of producers receiving emergency relief under this paragraph. .",
      "versionDate": "2025-03-18",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:06:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
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
          "measure-id": "id119hr2227",
          "measure-number": "2227",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2227v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>WOlf and Livestock Fairness Act of 2025 or the WOLF Act</strong> <strong>of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves.</p><p>Specifically, the bill directs the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP)\u00a0to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves. USDA must develop a formula to determine the amount of emergency relief to provide to a producer of livestock. Among other factors, the formula must take into consideration the herd size of the producer and the\u00a0average annual\u00a0increase in management costs for producers in the state due to Mexican gray wolves.</p><p>Additionally, the bill modifies USDA's Livestock Indemnity Program. In the case of attacks on livestock by Mexican gray wolves, the bill increases the\u00a0payment rate from 75% to 100% of the market value of the affected livestock.</p>"
        },
        "title": "WOLF Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2227.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>WOlf and Livestock Fairness Act of 2025 or the WOLF Act</strong> <strong>of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves.</p><p>Specifically, the bill directs the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP)\u00a0to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves. USDA must develop a formula to determine the amount of emergency relief to provide to a producer of livestock. Among other factors, the formula must take into consideration the herd size of the producer and the\u00a0average annual\u00a0increase in management costs for producers in the state due to Mexican gray wolves.</p><p>Additionally, the bill modifies USDA's Livestock Indemnity Program. In the case of attacks on livestock by Mexican gray wolves, the bill increases the\u00a0payment rate from 75% to 100% of the market value of the affected livestock.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr2227"
    },
    "title": "WOLF Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>WOlf and Livestock Fairness Act of 2025 or the WOLF Act</strong> <strong>of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves.</p><p>Specifically, the bill directs the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP)\u00a0to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves. USDA must develop a formula to determine the amount of emergency relief to provide to a producer of livestock. Among other factors, the formula must take into consideration the herd size of the producer and the\u00a0average annual\u00a0increase in management costs for producers in the state due to Mexican gray wolves.</p><p>Additionally, the bill modifies USDA's Livestock Indemnity Program. In the case of attacks on livestock by Mexican gray wolves, the bill increases the\u00a0payment rate from 75% to 100% of the market value of the affected livestock.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr2227"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2227ih.xml"
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
      "title": "WOLF Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WOLF Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WOlf and Livestock Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Act of 2014 to provide emergency relief to producers of livestock with herds adversely affected by Mexican gray wolves, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:21Z"
    }
  ]
}
```
