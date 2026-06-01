# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6388
- Title: Conservation Reserve Program Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 6388
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-16T08:07:41Z
- Update date including text: 2026-05-16T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6388",
    "number": "6388",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Conservation Reserve Program Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:41Z",
    "updateDateIncludingText": "2026-05-16T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:02:37Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6388ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6388\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Finstad introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to modernize the conservation reserve program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conservation Reserve Program Modernization Act .\n#### 2. Definitions\nSubchapter B of chapter 1 of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3831 et seq. ) is amended by inserting before section 1231 the following:\n1230. Definitions In this subchapter: (1) Conservation buffer The term conservation buffer means a practice that, once established, provides a benefit to water quality or another resource concern, including\u2014 (A) a grass sod waterway; (B) a contour grass sod strip; (C) a prairie strip; (D) a filterstrip; (E) a field border; (F) a living snow fence; (G) a riparian buffer; (H) a shelterbelt or windbreak; (I) a wetland or a wetland buffer (including a buffer for prairie potholes, a playa, or a pocosin); (J) a saturated buffer; (K) a bioreactor; (L) a wellhead protection area; and (M) other similar practices, as determined by the Secretary. (2) Eligible land The term eligible land means land that is authorized to be included in the conservation reserve program under section 1231(b). (3) Eligible partner The term eligible partner means\u2014 (A) a State; (B) a political subdivision of a State; (C) an Indian Tribe; or (D) a nongovernmental organization. (4) Land capability class The term land capability class means a soil classification assigned using the land capability classification system in effect on December 23, 1985. .\n#### 3. Eligible land\nSection 1231(b) of the Food Security Act of 1985 ( 16 U.S.C. 3831(b) ) is amended to read as follows:\n(b) Eligible land The Secretary may include in the conservation reserve program the following: (1) Cropland that\u2014 (A) (i) on a field level, consists of not less than 85 percent soils with a dryland cropland land capability class of III through VII; or (ii) cannot be farmed in accordance with a plan that complies with the requirements of subtitle B; and (B) the Secretary determines had a cropping history or was considered to be planted for not fewer than 4 of the 6 years preceding the date of enactment of the Conservation Reserve Program Modernization Act . (2) Cropland (including prairie potholes, playas, and pocosins within cropland), grasslands, and marginal pasture land (including marginal pastureland converted to wetland or established as wildlife habitat) to be\u2014 (A) devoted to conservation buffers; (B) established to ecologically appropriate vegetation, including trees, in or near riparian areas, intermittent, seasonal, or perennial streams, wetlands (including prairie potholes, playas, and pocosins), or saline-impaired soils; or (C) devoted to similar water quality or wildlife habitat practices. (3) Grasslands that\u2014 (A) contain forbs or shrubland (including improved rangeland and pastureland) for which grazing is the predominant use; (B) are located in an area historically dominated by grasslands; and (C) could provide habitat for animal and plant populations of significant ecological value if the land is retained in its current use or restored to a natural condition. (4) Land described in paragraph (1), (2), or (3) that will address significant water quality, water conservation, and wildlife habitat concerns, as proposed by an eligible partner and agreed to by the Secretary for purposes of section 1231A. (5) The portion of land in a field not enrolled in the conservation reserve in a case in which\u2014 (A) more than 50 percent of the land in the field is enrolled as a buffer or filterstrip, or more than 75 percent of the land in the field is enrolled as a conservation practice other than as a buffer or filterstrip; and (B) the Secretary determines that the remainder of the field is infeasible to farm. .\n#### 4. Payments\n##### (a) Cost sharing payments\nSection 1234(b)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3834(b)(1) ) is amended to read as follows:\n(1) In general In making cost-sharing payments to an owner or operator under a contract entered into under this subchapter, the Secretary shall pay 50 percent of the cost of, as the Secretary determines appropriate and in the public interest\u2014 (A) establishing permanent vegetation, including site preparation, cover, fertilizer, seeding, and planting; (B) carrying out erosion control practices necessary to stabilize the site for vegetation established under subparagraph (A); (C) installing fencing to protect riparian areas and buffers; (D) carrying out water development practices associated with excluding livestock from protected riparian areas; (E) installing fencing and carrying out water development practices to facilitate transition to livestock grazing on lands enrolled under the grasslands enrollment option; (F) conducting the necessary and appropriate mid-contract management activities to maintain the permanent cover and associated benefits; and (G) carrying out other water quality conservation measures and practices. .\n##### (b) Annual rental payments\n**(1) Multiple enrollments**\nSection 1234(d)(2)(B) of the Food Security Act of 1985 ( 16 U.S.C. 3834(d)(2)(B) ) is amended to read as follows:\n(B) Multiple enrollments (i) In general Notwithstanding subparagraph (A), if land subject to a contract entered into under this subchapter is reenrolled pursuant to section 1231(h), the annual rental payment shall be in an amount that is not more than the applicable percentage of the relevant county average soil rental rate for the year in which the reenrollment occurs (as determined under paragraph (4)(E)). (ii) Applicable percentage For purposes of clause (i), the applicable percentage shall be\u2014 (I) for the first reenrollment that occurs after the date of enactment the Conservation Reserve Program Modernization Act , 85 percent; and (II) for each subsequent reenrollment, the percentage that is 10 percentage points less than the percentage that was applicable to the preceding reenrollment. .\n**(2) Rental rate limitation**\nSection 1234(d)(4)(E) of the Food Security Act of 1985 ( 16 U.S.C. 3834(d)(4)(E) ) is amended to read as follows:\n(E) Rental rate limitation The county average soil rental rate (before any adjustments relating to specific practices, wellhead protection, or soil productivity) shall not exceed\u2014 (i) for eligible land consisting of soils with a dryland cropland land capability class of I or II that is enrolled under the general enrollment option or the conservation reserve enhancement program, 85 percent of the estimated rental rate determined under this paragraph; (ii) for eligible land consisting of soils with a dryland cropland land capability class of III that is enrolled under the general enrollment option or the conservation reserve enhancement program, 100 percent of the estimated rental rate determined under this paragraph; (iii) for eligible land consisting of soils with a dryland cropland land capability class of IV through VII that is enrolled under the general enrollment option or the conservation reserve enhancement program, 115 percent of the estimated rental rate determined under this paragraph; and (iv) for eligible land enrolled under the continuous enrollment option, 100 percent of the estimated rental rate determined under this paragraph, without regard to the land capability class of the soil. .",
      "versionDate": "2025-12-03",
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
        "updateDate": "2025-12-04T17:20:24Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6388ih.xml"
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
      "title": "Conservation Reserve Program Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T09:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Conservation Reserve Program Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T09:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to modernize the conservation reserve program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T09:18:37Z"
    }
  ]
}
```
