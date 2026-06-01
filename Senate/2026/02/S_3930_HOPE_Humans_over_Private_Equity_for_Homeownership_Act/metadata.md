# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3930?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3930
- Title: HOPE (Humans over Private Equity) for Homeownership Act
- Congress: 119
- Bill type: S
- Bill number: 3930
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-03-18T18:16:13Z
- Update date including text: 2026-03-18T18:16:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3930",
    "number": "3930",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "HOPE (Humans over Private Equity) for Homeownership Act",
    "type": "S",
    "updateDate": "2026-03-18T18:16:13Z",
    "updateDateIncludingText": "2026-03-18T18:16:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T16:42:30Z",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3930is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3930\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. Merkley (for himself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose an excise tax on the acquisition of single-family residences by hedge fund taxpayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the HOPE (Humans over Private Equity) for Homeownership Act .\n#### 2. Excise tax on acquisition of single-family residences by hedge fund taxpayers\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Single-family residences Sec. 5000E. Newly acquired single-family residences. 5000E. Newly acquired single-family residences (a) In general There is hereby imposed the acquisition of any newly acquired single-family residence by a hedge fund taxpayer an amount equal to 15 percent of the purchase price thereof. (b) Newly acquired single-Family residence For purposes of this section\u2014 (1) In general The term newly acquired single-family residence means any residential property which\u2014 (A) consists of 1-to-4 dwelling units, and (B) was acquired by the taxpayer in any taxable year which begins after the date of the enactment of this chapter. (2) Exception A residential property shall not be treated as a newly acquired single-family residence if, immediately after acquisition and at all times thereafter, such property is\u2014 (A) not rented or leased, and (B) used as the principal residence (within the meaning of section 121) of any person who has an ownership interest in the hedge fund taxpayer acquiring such taxpayer. (c) Hedge fund taxpayer For purposes of this chapter\u2014 (1) In general The term hedge fund taxpayer means, with respect to any taxable year, any applicable entity which\u2014 (A) manages funds pooled from investors, (B) has $50,000,000 or more in net value or assets under management on any day during the taxable year, and (C) is a fiduciary with respect to such investors. (2) Applicable entity (A) In general The term applicable entity means\u2014 (i) any partnership, (ii) any corporation, or (iii) any real estate investment trust. (B) Exceptions The term applicable entity shall not include\u2014 (i) an organization which is described in section 501(c)(3) and exempt from tax under section 501(a), or (ii) an organization which is primarily engaged in the construction or rehabilitation of single-family residences and which offers such residences for sale in the ordinary course of business. (3) Aggregation rules (A) In general All persons which are treated as a single employer under subsections (a) and (b) of section 52 shall be treated as a single person. (B) Modifications For purposes of this subsection\u2014 (i) section 52(a) shall be applied by substituting component members for members , and (ii) for purposes of applying section 52(b), the term trade or business shall include any activity treated as a trade or business under paragraph (5) or (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations in such paragraph (6)). (C) Component member For purposes of this paragraph, the term component member has the meaning given such term by section 1563(b), except that the determination shall be made without regard to section 1563(b)(2). (d) Other definitions and rules For purposes of this section\u2014 (1) Purchase price The term purchase price means the adjusted basis of the newly acquired single-family residence on the date such residence is purchased. (2) Acquisition A hedge fund taxpayer shall be treated as acquiring a single-family residence if the taxpayer acquires a majority ownership interest in the single-family residence, regardless of the percentage of that ownership interest. .\n##### (b) Clerical amendment\nThe table of chapters for subtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nChapter 50B\u2014Excess single-family residences .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.\n#### 3. Corporate surtax on hedge fund taxpayers\n##### (a) In general\nSection 11 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(e) Hedge fund taxpayers In the case of a corporation which is described in section 5000E(c), the percentage under subsection (b) shall be increased by 5 percentage points. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2035.\n#### 4. Disallowance of certain deductions taken in connection with single-family residences of hedge fund taxpayers\n##### (a) Mortgage interest\n**(1) In general**\nSection 163 of the Internal Revenue Code of 1986 is amended by redesignating subsection (n) as subsection (o) and by inserting after subsection (m) the following new subsection:\n(n) No deduction for interest on acquisition indebtedness of single-Family residences of certain taxpayers (1) In general In the case of a hedge fund taxpayer, no deduction shall be allowed under this chapter with respect to interest paid or accrued on acquisition indebtedness with respect to any single-family residence. (2) Definitions For purposes of this subsection\u2014 (A) Hedge fund taxpayer The term hedge fund taxpayer means, for any taxable year, any taxpayer\u2014 (i) who is described in section 5000E(c), and (ii) who is in the trade or business of renting or leasing single-family residences. (B) Acquisition indebtedness The term acquisition indebtedness has the meaning given such term under subsection (h)(3)(B), determined\u2014 (i) by substituting single-family residence (as defined in subsection (n)) for qualified residence , and (ii) without regard to clause (ii) thereof. (C) Single-family residence The term single-family residence means any residential property which consists of 1-to-4 dwelling units. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to taxable years beginning after December 31, 2030.\n##### (b) Depreciation\n**(1) In general**\nSection 167 of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Deduction disallowed for single-Family residences of certain taxpayers (1) In general In the case of a hedge fund taxpayer, no deduction shall be allowed under this section for any single-family residence. (2) Definitions For purposes of this subsection\u2014 (A) Hedge fund taxpayer The term hedge fund taxpayer means, for any taxable year, any taxpayer\u2014 (i) who is described in section 5000E(c), and (ii) who is in the trade or business of renting or leasing single-family residences. (B) Single-family residence The term single-family residence means any residential property which consists of 1-to-4 dwelling units. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to taxable years beginning after December 31, 2030.\n##### (c) Qualified business income\n**(1) In general**\nSection 199A(d)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (A), by striking the period at the end of subparagraph (B) and inserting , or , and by adding at the end the following new subparagraph:\n(C) any trade or business of hedge fund taxpayer (as defined in section 163(n)(2)(A)). .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to taxable years beginning after December 31, 2035.",
      "versionDate": "2026-02-26",
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
        "updateDate": "2026-03-18T18:16:13Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3930is.xml"
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
      "title": "HOPE (Humans over Private Equity) for Homeownership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HOPE (Humans over Private Equity) for Homeownership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to impose an excise tax on the acquisition of single-family residences by hedge fund taxpayers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T03:48:27Z"
    }
  ]
}
```
