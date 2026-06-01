# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1745
- Title: HOPE for Homeownership Act
- Congress: 119
- Bill type: HR
- Bill number: 1745
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-02-25T09:06:31Z
- Update date including text: 2026-02-25T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1745",
    "number": "1745",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "HOPE for Homeownership Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:31Z",
    "updateDateIncludingText": "2026-02-25T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:16:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NH"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1745ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1745\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Smith of Washington (for himself and Ms. S\u00e1nchez ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose an excise tax on the failure of certain hedge funds owning excess single-family residences to dispose of such residences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humans over Private Equity for Homeownership Act or the HOPE for Homeownership Act .\n#### 2. Excise tax on certain taxpayers failing to sell excess single-family residences\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Excess single-family residences Sec. 5000E. Newly acquired single-family residences. Sec. 5000F. Excess single-family residences. Sec. 5000G. Definitions and other special rules. 5000E. Newly acquired single-family residences (a) In general In the case of a hedge fund taxpayer, there is hereby imposed a tax on the acquisition of any newly acquired single-family residence equal to the greater of\u2014 (1) 15 percent of the purchase price, or (2) $10,000 (b) Newly acquired Single-Family residence For purposes of this section, the term newly acquired single-family residence means any single-family residence which was acquired by the taxpayer in any taxable year which begins after the date of the enactment of this chapter. (c) Purchase price For purposes of this section, the term purchase price means the adjusted basis of the newly acquired single-family residence on the date such residence is purchased. 5000F. Excess single-family residences (a) In general In the case of an applicable taxpayer who fails to meet the requirements of subsection (b), there is hereby imposed a tax equal to the product of\u2014 (1) $5,000, and (2) the excess of\u2014 (A) the number of applicable single-family residences owned by the taxpayer as of the last day of the taxable year, over (B) the maximum permissible units for the taxable year. (b) Requirement (1) In general An applicable taxpayer meets the requirement of this subsection for any taxable year if the number of applicable single-family residences owned by the taxpayer as of the last day of the taxable year is equal to or less than the maximum permissible units determined with respect to such taxpayer for such taxable year. (2) Special rule for certain sales For purposes of applying paragraph (1), a single-family residence which is sold or transferred in a disqualified sale during the taxable year shall be treated as a single-family residence which is owned by the applicable taxpayer as of the last day of such taxable year. (c) Maximum permissible units The maximum permissible units with respect to any applicable taxpayer for any taxable year shall be determined as follows: In the case of\u2014 The maximum permissible units for a hedge fund taxpayer is\u2014 The maximum permissible units for any other applicable taxpayer is\u2014 the first full taxable year beginning after the applicable date . . . 90 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 90 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the second taxable year beginning after the applicable date . . . 80 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 80 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the third taxable year beginning after the applicable date . . . 70 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 70 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the fourth taxable year beginning after the applicable date . . . 60 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 60 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the fifth taxable year beginning after the applicable date . . . 50 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 50 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the sixth taxable year beginning after the applicable date . . . 40 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 40 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the seventh taxable year beginning after the applicable date . . . 30 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 30 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the eighth taxable year beginning after the applicable date . . . 20 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 20 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date the ninth taxable year beginning after the applicable date . . . 10 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date 50 plus 10 percent of the number of applicable single-family residences owned by the taxpayer on the applicable date any taxable year beginning more than 9 years after the applicable date . . . 0 50. (d) Definitions For purposes of this section\u2014 (1) Applicable single-family residence The term applicable single-family residence means any single-family residence which was acquired on or before the applicable date. (2) Applicable date (A) In general The term applicable date means\u2014 (i) the last day of the first full taxable year ending on or after the date of the enactment of this chapter, or (ii) in the case of any taxpayer described in subparagraph (B), the date provided in such subparagraph. (B) Taxpayers changing status (i) In general In the case of any applicable taxpayer described in clause (ii), the applicable date means the last day of the taxable year immediately preceding the taxable year in which the taxpayer is described in such clause. (ii) Applicable taxpayer described An applicable taxpayer is described in this clause with respect to any taxable year if\u2014 (I) such taxpayer was not a hedge fund taxpayer for the preceding taxable year, and (II) such taxpayer is a hedge fund taxpayer for such taxable year. (3) Disqualified sale The term disqualified sale means any sale or transfer to\u2014 (A) a corporation or other entity engaged in a trade or business, or (B) an individual who owns any other single-family residence at the time of such sale or transfer. 5000G. Definitions and other special rules (a) Applicable taxpayer For purposes of this chapter\u2014 (1) In general The term applicable taxpayer means any applicable entity which\u2014 (A) manages funds pooled from investors, and (B) is a fiduciary with respect to such investors. (2) Applicable entity (A) In general The term applicable entity means\u2014 (i) any partnership, (ii) any corporation, or (iii) any real estate investment trust. (B) Exceptions The term applicable entity shall not include\u2014 (i) an organization which is described in section 501(c)(3) and exempt from tax under section 501(a), or (ii) an organization which is primarily engaged in the construction or rehabilitation of single-family residences and which offers such residences for sale in the ordinary course of business. (b) Hedge fund taxpayer For purposes of this section, the term hedge fund taxpayer means, with respect to any taxable year, any applicable taxpayer which has $50,000,000 or more in net value or assets under management on any day during the taxable year. (c) Single-Family residence For purposes of this chapter\u2014 (1) In general The term single-family residence means a residential property consisting of 1-to-4 dwelling units. (2) Exceptions A residential property shall not be treated as a residential property described in clause (i) if\u2014 (A) such property is unoccupied and acquired through foreclosure (other than such a residence acquired through foreclosure by a hedge fund taxpayer, as defined in section 5000F((d)(3)), (B) such property is\u2014 (i) not rented or leased, and (ii) used as the principal residence (within the meaning of section 121) of any person who has an ownership interest in the applicable taxpayer, or (C) such property\u2014 (i) was a building with respect to which a credit was allowed under section 42 (relating to the low-income housing credit), and (ii) is not owned by a hedge fund taxpayer (as defined in section 5000F(d)(3)). (d) Acquisition; ownership For purposes of this chapter, an applicable taxpayer shall be treated\u2014 (1) as acquiring a single-family residence if the applicable taxpayer acquires a majority ownership interest in the single-family residence, regardless of the percentage of that ownership interest, and (2) as owning a single-family residence if the applicable taxpayer owns a majority ownership interest in the single-family residence, regardless of the percentage of that ownership interest. (e) Aggregation rules (1) In general For purposes of this chapter, all persons which are treated as a single employer under subsections (a) and (b) of section 52 shall be treated as a single person. (2) Modifications For purposes of this subsection\u2014 (A) section 52(a) shall be applied by substituting component members for members , and (B) for purposes of applying section 52(b), the term trade or business shall include any activity treated as a trade or business under paragraph (5) or (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations in such paragraph (6)). (3) Component member For purposes of this paragraph, the term component member has the meaning given such term by section 1563(b), except that the determination shall be made without regard to section 1563(b)(2). .\n##### (b) Clerical amendment\nThe table of chapters for subtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nChapter 50B\u2014Excess single-family residences .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.\n#### 3. Disallowance of mortgage interest and depreciation in connection with single family residences owned by covered taxpayers\n##### (a) Mortgage interest\n**(1) In general**\nSection 163 of the Internal Revenue Code of 1986 is amended by redesignating subsection (n) as subsection (o) and by inserting after subsection (m) the following new subsection:\n(n) Certain interest paid by covered taxpayers (1) In general No deduction shall be allowed under this chapter for a taxable year with respect to interest paid or accrued on acquisition indebtedness with respect to any single-family residence if the owner of such single-family residence is liable for tax under chapter 50B for such taxable year. (2) Definitions For purposes of this subsection\u2014 (A) Acquisition indebtedness The term acquisition indebtedness has the meaning given such term under subsection (h)(3)(B), determined\u2014 (i) by substituting single-family residence (as defined in section 5000G(b)) for qualified residence , and (ii) without regard to clause (ii) thereof. (B) Single-family residence The term single-family residence has the meaning given such term under section 5000G(b) (C) Ownership The rules of section 5000G(c) shall apply for purposes of determining ownership. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to taxable years beginning after the date of the enactment of this Act.\n##### (b) Depreciation\n**(1) In general**\nSection 167 of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Deduction disallowed for disqualified single family property owners (1) In general No deduction shall be allowed under this section for a taxable year with respect to a single-family residence if the owner of such single-family residence is liable for tax under chapter 50B for such taxable year. (2) Definitions For purposes of this subsection\u2014 (A) Single-family residence The term single-family residence has the meaning given such term under section 5000G(b). (B) Ownership The rules of section 5000G(c) shall apply for purposes of determining ownership. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "788",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HOPE (Humans over Private Equity) for Homeownership Act",
      "type": "S"
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
        "updateDate": "2025-05-08T18:37:19Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1745ih.xml"
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
      "title": "HOPE for Homeownership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T14:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOPE for Homeownership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T14:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Humans over Private Equity for Homeownership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T14:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to impose an excise tax on the failure of certain hedge funds owning excess single-family residences to dispose of such residences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T14:03:36Z"
    }
  ]
}
```
