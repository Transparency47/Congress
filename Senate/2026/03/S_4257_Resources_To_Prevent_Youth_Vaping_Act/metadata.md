# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4257
- Title: Resources To Prevent Youth Vaping Act
- Congress: 119
- Bill type: S
- Bill number: 4257
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-14T11:03:26Z
- Update date including text: 2026-04-14T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4257",
    "number": "4257",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Resources To Prevent Youth Vaping Act",
    "type": "S",
    "updateDate": "2026-04-14T11:03:26Z",
    "updateDateIncludingText": "2026-04-14T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T20:49:41Z",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AK"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4257is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4257\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mrs. Shaheen (for herself, Ms. Murkowski , Mr. Durbin , Ms. Baldwin , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo apply user fees with respect to tobacco products deemed subject to the requirements of chapter IX of the Federal Food, Drug, and Cosmetic Act.\n#### 1. Short title\nThis Act may be cited as the Resources To Prevent Youth Vaping Act .\n#### 2. User fees\n##### (a) Increase in total amount\nSection 919(b)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b)(1) ) is amended by striking subparagraph (K) and inserting the following subparagraphs:\n(K) For each of fiscal years 2019 through 2026, $712,000,000. (L) For fiscal year 2027, $826,200,000. (M) For fiscal year 2028 and each subsequent fiscal year, the amount that was applicable for the previous fiscal year, adjusted by the total percentage change that occurred in the Consumer Price Index for all urban consumers (all items; United States city average) for the 12-month period ending June 30 preceding the fiscal year. .\n##### (b) Application of user fees to all classes of tobacco products\n**(1) In general**\nSubparagraph (A) of section 919(b)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b)(2) ) is amended to read as follows:\n(A) In general (i) Fiscal years 2027 and 2028 For fiscal years 2027 and 2028, user fees shall be assessed and collected under subsection (a) only with respect to the classes of tobacco products listed in subparagraph (B)(i), and the total such user fees with respect to each such class shall be an amount that is equal to the applicable percentage of each such class for the fiscal year multiplied by the amount specified in paragraph (1) for the fiscal year. (ii) Subsequent fiscal years For fiscal year 2029 and each subsequent fiscal year, user fees shall be assessed and collected under subsection (a) with respect to each class of tobacco products to which this chapter applies (including tobacco products that the Secretary by regulation deems to be subject to this chapter), and the total user fees with respect to each such class shall be\u2014 (I) with respect to each class of tobacco products listed in subparagraph (B)(i), an amount that is calculated in the same way as the amounts calculated for fiscal years 2027 and 2028 under clause (i), except that for purposes of fiscal years 2029 and subsequent fiscal years, instead of multiplying the applicable percentage of each such class by the amount specified in paragraph (1) for the fiscal year , the applicable percentage shall be multiplied by\u2014 (aa) the amount specified in paragraph (1) for the fiscal year, reduced by (bb) the total user fees assessed and collected pursuant to subparagraph (C) for the fiscal year; and (II) with respect to each class of tobacco products to which this chapter applies but which is not listed in subparagraph (B)(i), an amount determined pursuant to a formula under subparagraph (C). .\n**(2) Other tobacco products**\nSection 919(b)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b)(2) ), as amended by paragraph (1), is further amended by adding at the end the following new subparagraphs:\n(C) Allocation for other tobacco products (i) In general Beginning with fiscal year 2029, the total user fees assessed and collected under subsection (a) each fiscal year with respect to each class of tobacco products not listed in subparagraph (B)(i) shall be an amount that is determined pursuant to a formula developed by the Secretary by regulation using information required to be submitted under subparagraph (D). (ii) Allocation for other tobacco products For each class of tobacco products not listed in subparagraph (B)(i), the percentage of fees under the formula under clause (i) for the respective fiscal year shall be equal to the percentage of the gross domestic sales in the previous calendar year that is attributable to such class of tobacco products in such calendar year, as determined by the Secretary. (iii) Allocation of assessment within each class of other tobacco products The percentage of the total user fees to be paid by each manufacturer or importer of tobacco products in a class not listed in subparagraph (B)(i) shall be determined by the Secretary, based on the percentage of the gross domestics sales of all such classes of tobacco products by all manufacturers and importers in the previous calendar year that is attributable to such manufacturer or importer. (iv) Effect of failure to finalize formula on time If the Secretary for any reason fails to finalize by fiscal year 2029 the formula required by this subparagraph for the assessment and collection of user fees for classes of tobacco products not listed in subparagraph (B)(i)\u2014 (I) the Secretary shall continue to assess and collect fees under subsection (a) with respect to each class of tobacco products listed in subparagraph (B)(i); and (II) until the first fiscal year commencing after the finalization of such formula, the exception described in subparagraph (A)(ii)(I) shall not apply. (v) Revisions by regulation Any revisions to the formula promulgated pursuant to this subparagraph shall be by regulation. (vi) Definition In this subparagraph, the term gross domestic sales means the total value in dollars of the sale or distribution by manufacturers and importers of tobacco products in the United States in classes not listed in subparagraph (B)(i), as determined based on the aggregation of sales data from every manufacturer and importer of tobacco products that submits sales data to the Secretary. (D) Information required to be submitted Each manufacturer or importer of any tobacco product shall submit to the Secretary the information required under this subparagraph by March 1, 2028, for calendar year 2027, by April 1, 2028, for the period of January 1, 2028, through March 31, 2028, and monthly thereafter. Such information shall include\u2014 (i) the identification of the manufacturer or importer; (ii) the class or classes of tobacco products sold by the manufacturer or importer; (iii) the full listing of the finished tobacco products in a class not listed in subparagraph (B)(i) sold or distributed by the manufacturer or importer in the United States; and (iv) the gross domestic sales data for each class of finished tobacco products sold or distributed by the manufacturer or importer in the United States. .\n**(3) Prohibited act**\nSection 301(q)(1)(B) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331(q)(1)(B) ) is amended by inserting 919(b)(2)(D), before or 920 .\n##### (c) Allocation of assessment within each class of tobacco product\nSection 919(b)(4) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b)(4) ) is amended by striking shall be the percentage determined for purposes of allocations under subsections (e) through (h) of section 625 of Public Law 108\u2013357 and inserting shall be the percentage determined by the Secretary .\n##### (d) Conforming amendments\nSection 919(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b) ) is amended\u2014\n**(1)**\nby striking paragraph (5);\n**(2)**\nby redesignating paragraphs (6) and (7) as paragraphs (5) and (6), respectively; and\n**(3)**\nby amending paragraph (6), as redesignated, to read as follows:\n(6) Memorandum of understanding The Secretary shall request the appropriate Federal agency to enter into a memorandum of understanding that provides for the regular and timely transfer from the head of such agency to the Secretary of all necessary information regarding all tobacco product manufacturers and importers required to pay user fees. The Secretary shall maintain all disclosure restrictions established by the head of such agency regarding the information provided under the memorandum of understanding. .\n##### (e) Applicability\nThe amendments made by subsections (b), (c), and (d) shall apply beginning with fiscal year 2029. Except for the amendment made by subsection (a), section 919 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s ), as in effect on the day before the date of enactment of this Act, shall apply with respect to fiscal years preceding fiscal year 2029.\n#### 3. Annual reporting on tobacco regulation activities\n##### (a) In general\nSection 112(b) of division P of the Consolidated Appropriations Act, 2022 ( 21 U.S.C. 387v(b) ) is amended by adding at the end the following:\n(12) A breakdown of the amount expended on activities related to deemed tobacco products versus the amount expended on activities related to combustible tobacco products listed in section 919(b)(2)(B)(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b)(2)(B)(i) ). (13) An explanation for how the Food and Drug Administration ensures that the amount of user fees allocated to public education campaigns on youth e-cigarette use and prevention is sufficient to meet the need for education of teens and minors on the dangers of e-cigarettes and other Electronic Nicotine Delivery Systems (commonly referred to as ENDS ). (14) When applicable, a breakdown of the amount or user fees collected under the amendments made by this Act from manufacturers of deemed tobacco products and the amount collected from manufacturers of each of the original pre-existing categories of tobacco products under section 919(b)(2)(B)(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 387s(b)(2)(B)(i) ). .\n##### (b) Application\nThe information described in paragraphs (12) and (13) of subsection (b) of section 112 of division P of the Consolidated Appropriations Act, 2022 ( 21 U.S.C. 387v(b) ), as added by subsection (a), shall be required to be included in reports under such section 112 for fiscal year 2027 and each subsequent fiscal year, and the information described in paragraph (14) of such section 112, as added by subsection (a), shall be required to be included in reports under such section 112 for fiscal year 2029 and each subsequent fiscal year.",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-04-13T13:32:14Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4257is.xml"
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
      "title": "Resources To Prevent Youth Vaping Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Resources To Prevent Youth Vaping Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to apply user fees with respect to tobacco products deemed subject to the requirements of chapter IX of the Federal Food, Drug, and Cosmetic Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:18:26Z"
    }
  ]
}
```
