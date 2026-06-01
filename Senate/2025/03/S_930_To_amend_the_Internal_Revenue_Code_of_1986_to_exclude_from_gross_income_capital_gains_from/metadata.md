# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/930?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/930
- Title: A bill to amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans.
- Congress: 119
- Bill type: S
- Bill number: 930
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-02-05T15:17:29Z
- Update date including text: 2026-02-05T15:17:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/930",
    "number": "930",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000355",
        "district": "",
        "firstName": "Mitch",
        "fullName": "Sen. McConnell, Mitch [R-KY]",
        "lastName": "McConnell",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans.",
    "type": "S",
    "updateDate": "2026-02-05T15:17:29Z",
    "updateDateIncludingText": "2026-02-05T15:17:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T15:51:13Z",
          "name": "Referred To"
        }
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "WV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s930is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 930\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. McConnell introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans.\n#### 1. Exclusion of certain capital gains from the sale of certain farmland property\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Gain from the sale or exchange of qualified farmland property to qualified farmers (a) In general If a taxpayer makes an election under this section and files the agreement referred to in subsection (d)(2), gross income shall not include so much of the gain from the sale or exchange of qualified farmland property to a qualified farmer as does not exceed the aggregate amount contributed by the taxpayer to an individual retirement plan during the 60-day period beginning on the date of such sale or exchange. (b) Qualified farmland property; qualified farmer For purposes of this section\u2014 (1) Qualified farmland property The term qualified farmland property means real property located in the United States which\u2014 (A) has been used by the taxpayer as a farm for farming purposes, or (B) leased by the taxpayer to a farmer for farming purposes, during substantially all of the 10-year period ending on the date of the qualified sale or exchange. (2) Qualified farmer The term qualified farmer means any individual who\u2014 (A) is actively engaged in farming (within the meaning of subsections (b) and (c) of section 1001 of the Food Security Act of 1986 ( 7 U.S.C. 1308\u20131(b) and (c))), and (B) is designated in an agreement under subsection (d)(2). (c) Tax treatment of further dispositions or non-Farm use (1) In general If, within 10 years after the date of the sale or exchange\u2014 (A) the qualified farmer disposes of any interest in qualified farmland property, or (B) the qualified farmer ceases to use the qualified farmland property as a farm for farming purposes, then, in addition to any other tax, there is hereby imposed for the taxable year of such disposition or cease in use, a tax in the amount determined under paragraph (2). (2) Amount of tax The amount of tax determined under this paragraph is an amount equal to the sum of\u2014 (A) the product of\u2014 (i) the amount excluded from the gross income under subsection (a), and (ii) the sum of\u2014 (I) the highest rate of tax on adjusted net capital gain under section 1(h), plus (II) the rate of tax applicable under section 1411, plus (B) interest at the underpayment rate established under section 6621 on the amount determined under subparagraph (A) for each prior taxable year for the period beginning with the taxable year in which the sale or exchange occurred. (3) Liability for tax The qualified farmer shall be personally liable for the additional tax imposed by this subsection. (4) Partial dispositions For purposes of this subsection, where the qualified farmer disposes of a portion of the qualified farmland acquired by such qualified farmer or there is a cessation of use of such a portion as a farm for farming purposes, the amount determined under paragraph (2)(A)(i) shall be the amount which bears the same ratio the amount otherwise determined under such paragraph as\u2014 (A) the portion of the qualified farmland so disposed or ceased to be used, bears to (B) the entire amount of the qualified farmland so acquired. (d) Election (1) In general An election under subsection (a) shall be made at such time and in such form and manner as the Secretary shall prescribe. Such an election, once made, shall be irrevocable. (2) Agreement The agreement referred to in this paragraph is a written agreement signed by the qualified farmer designated in such agreement consenting to the application of subsection (c) with respect to the qualified farmland property. Such agreement shall include a statement indicating the amount described in subsection (c)(2)(A)(i). (e) Definitions and special rules For purposes of this section\u2014 (1) Farm; farming purposes For purposes of this section, the terms farm and farming purposes have the respective meanings given such terms under section 2032A(e). (2) Statute of limitations If qualified farmland property is disposed of or ceases to be used as a farm for farming purposes, then\u2014 (A) the statutory period for the assessment of any tax under subsection (c) attributable to such disposition or cessation shall not expire before the expiration of 3 years from the date the Secretary is notified (in such manner as the Secretary may by regulations prescribe) of such disposition or cessation, and (B) such tax may be assessed before the expiration of such 3-year period notwithstanding the provisions of any other law or rule of law which would otherwise prevent such assessment. (3) Involuntary conversions and like-kind exchanges (A) Involuntary conversions Under regulations provided by the Secretary, no tax shall be imposed under subsection (c) if there is an involuntary conversion (within the meaning of section 2032A(h)(3) of an interest in qualified farmland property. (B) Like-kind exchanges Rules similar to the rules of section 2032A(i) shall apply where qualified farmland property is disposed of in a transaction which qualifies under section 1031. (4) No double benefit No deduction shall be allowed under section 219 with respect so much of the qualified retirement contributions for the taxable year as does not exceed the amount excluded from income under subsection (a). .\n##### (b) Waiver of contribution limitation\nSection 408 of the Internal Revenue Code of 1986 is amended by redesignating subsection (r) as subsection (s) and by inserting after subsection (q) the following new subsection:\n(r) Increased limitation for contributions of qualified farmland gain (1) In general For purposes of applying subsections (a)(1) and (b)(2)(B), the amount in effect under section 219(b)(1)(A) for any taxable year shall be increased by the lesser of\u2014 (A) the aggregate amount of gain by the taxpayer from the sale or exchange of qualified farmland property to a qualified farmer during the period beginning 60 days before the first day of such taxable year and ending with the last day of such taxable year, or (B) the amount contributed during the 60-day period ending with such sale or exchange to individual retirement plans of the taxpayer. (2) Definitions Any term used in this section which is used in section 139J shall have the meaning given such term under such section. .\n##### (c) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Gain from the sale or exchange of qualified farmland property to qualified farmers. .\n##### (d) Effective date\nThe amendments made by this section shall apply to sales or exchanges in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-11",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T13:51:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s930",
          "measure-number": "930",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-02-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s930v00",
            "update-date": "2026-02-05"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill excludes from gross income the gain from the sale or exchange of qualified farmland property to a qualified farmer that is contributed to an individual retirement account (IRA). This generally\u00a0prevents the federal capital gains tax from being imposed on such gain. (Conditions apply.)</p><p>Specifically, the bill excludes from gross income any gain from the sale or exchange of qualified farmland property contributed to an IRA within 60 days of the sale or exchange if\u00a0</p><ul><li>the requisite election is made,</li><li>the property is sold to an individual actively engaged in farming (qualified farmer),</li><li>the qualified farmer signs a written agreement consenting to the application of a federal tax if the property is disposed of or no longer used for farming within the first 10 years after the sale or exchange, and</li><li>the written agreement is filed.</li></ul><p>The bill defines <em>qualified farmland property</em> as real property located in the United States that, for substantially all of the 10 years preceding the sale or exchange, is used by the farmer (or lessee) for farming purposes.</p><p>However, under the bill, if the qualified farmland property is disposed of or no longer used for farming within the first 10 years after the sale or exchange, a tax is imposed on the qualified farmer equal to the amount excluded from gross income multiplied by\u00a0the sum of the highest tax rate on adjusted net capital gains and the net investment income tax rate\u00a0(currently 23.8%), plus interest.</p>"
        },
        "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s930.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill excludes from gross income the gain from the sale or exchange of qualified farmland property to a qualified farmer that is contributed to an individual retirement account (IRA). This generally\u00a0prevents the federal capital gains tax from being imposed on such gain. (Conditions apply.)</p><p>Specifically, the bill excludes from gross income any gain from the sale or exchange of qualified farmland property contributed to an IRA within 60 days of the sale or exchange if\u00a0</p><ul><li>the requisite election is made,</li><li>the property is sold to an individual actively engaged in farming (qualified farmer),</li><li>the qualified farmer signs a written agreement consenting to the application of a federal tax if the property is disposed of or no longer used for farming within the first 10 years after the sale or exchange, and</li><li>the written agreement is filed.</li></ul><p>The bill defines <em>qualified farmland property</em> as real property located in the United States that, for substantially all of the 10 years preceding the sale or exchange, is used by the farmer (or lessee) for farming purposes.</p><p>However, under the bill, if the qualified farmland property is disposed of or no longer used for farming within the first 10 years after the sale or exchange, a tax is imposed on the qualified farmer equal to the amount excluded from gross income multiplied by\u00a0the sum of the highest tax rate on adjusted net capital gains and the net investment income tax rate\u00a0(currently 23.8%), plus interest.</p>",
      "updateDate": "2026-02-05",
      "versionCode": "id119s930"
    },
    "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans."
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill excludes from gross income the gain from the sale or exchange of qualified farmland property to a qualified farmer that is contributed to an individual retirement account (IRA). This generally\u00a0prevents the federal capital gains tax from being imposed on such gain. (Conditions apply.)</p><p>Specifically, the bill excludes from gross income any gain from the sale or exchange of qualified farmland property contributed to an IRA within 60 days of the sale or exchange if\u00a0</p><ul><li>the requisite election is made,</li><li>the property is sold to an individual actively engaged in farming (qualified farmer),</li><li>the qualified farmer signs a written agreement consenting to the application of a federal tax if the property is disposed of or no longer used for farming within the first 10 years after the sale or exchange, and</li><li>the written agreement is filed.</li></ul><p>The bill defines <em>qualified farmland property</em> as real property located in the United States that, for substantially all of the 10 years preceding the sale or exchange, is used by the farmer (or lessee) for farming purposes.</p><p>However, under the bill, if the qualified farmland property is disposed of or no longer used for farming within the first 10 years after the sale or exchange, a tax is imposed on the qualified farmer equal to the amount excluded from gross income multiplied by\u00a0the sum of the highest tax rate on adjusted net capital gains and the net investment income tax rate\u00a0(currently 23.8%), plus interest.</p>",
      "updateDate": "2026-02-05",
      "versionCode": "id119s930"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s930is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:28Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income capital gains from the sale of certain farmland property which are reinvested in individual retirement plans.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T10:56:27Z"
    }
  ]
}
```
