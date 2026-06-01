# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2912?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2912
- Title: Oligarch Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2912
- Origin chamber: House
- Introduced date: 2025-04-14
- Update date: 2025-05-14T08:05:56Z
- Update date including text: 2025-05-14T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-14: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-14: Introduced in House

## Actions

- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-14",
    "latestAction": {
      "actionDate": "2025-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2912",
    "number": "2912",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Oligarch Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-14T08:05:56Z",
    "updateDateIncludingText": "2025-05-14T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
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
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-14",
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
          "date": "2025-04-14T13:01:10Z",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "DC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "IL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NJ"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "TX"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2912ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2912\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2025 Ms. Lee of Pennsylvania (for herself, Ms. Tlaib , Mr. Nadler , Mr. Frost , Ms. Norton , Ms. Dean of Pennsylvania , Mrs. Ramirez , Mr. Huffman , Mrs. Foushee , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a wealth tax, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Oligarch Act of 2025 .\n#### 2. Imposition of wealth tax\n##### (a) In general\nThe Internal Revenue Code of 1986 is amended by inserting after subtitle B the following new subtitle:\nB\u20131 Wealth tax Chapter 18\u2014Determination of wealth tax 18 Determination of wealth tax Sec. 2901. Imposition of tax. Sec. 2902. Net value of taxable assets. Sec. 2903. Special rules. Sec. 2904. Information reporting. Sec. 2905. Enforcement. 2901. Imposition of tax (a) In general In the case of any applicable taxpayer, a tax is hereby imposed on the net value of all taxable assets of the taxpayer on the last day of any calendar year. (b) Computation of tax (1) Individuals In the case of an individual, the tax imposed by this section shall be equal to the sum of\u2014 (A) 2 percent of so much of the net value of all taxable assets of the taxpayer as exceed the threshold amount but do not exceed the product of 10 multiplied by threshold amount, (B) 4 percent of so much of the net value of all taxable assets of the taxpayer as exceed the product of 10 multiplied by the threshold amount but do not exceed the product of 100 multiplied by the threshold amount, (C) 6 percent of so much of the net value of all taxable assets of the taxpayer as exceed the product of 100 multiplied by the threshold amount but do not exceed the product of 1,000 multiplied by the threshold amount, plus (D) 8 percent of so much of the net value of all taxable assets of the taxpayer as exceed the product of 1,000 multiplied by the threshold amount. (2) Trusts In the case of a trust, the tax imposed by this section shall be equal to 8 percent of so much of the net value of all taxable assets of the taxpayer as exceed the threshold amount. (c) Applicable taxpayer (1) In general The term applicable taxpayer means any individual or any trust (other than a trust described in section 401(a) and exempt from tax under section 501(a)). (2) Treatment of married individuals For purposes of this section, individuals who are married (as defined in section 7703) shall be treated as one applicable taxpayer. (d) Threshold amount For purposes of this section, the term threshold amount means the amount that is the product of 1,000 multiplied by the greater of\u2014 (1) $50,000, or (2) the applicable median household wealth. (e) Applicable median household wealth The Secretary shall annually determine the median household wealth with respect to the United States for purposes of this section. (f) Application to trusts (1) Attribution of assets in trust In determining the assets of a taxpayer for purposes of subsection (a): (A) Grantor trust In the case of a grantor trust, the grantor shall be treated as holding all the assets of the trust. (B) Beneficiary trust In the case of a beneficiary trust, each beneficiary of the trust shall be treated as holding a fraction of the assets of the trust in proportion to such beneficiary\u2019s interest in such trust. (2) Property of trusts Any asset treated as held by a grantor or beneficiary under paragraph (1) shall not be treated as held by the trust for purposes of this section. (3) Trusts relating to common beneficiaries Trusts benefitting substantially the same beneficiaries shall be treated as a single applicable taxpayer for purposes of this section. (4) Definitions For purposes of this section: (A) Grantor trust The term grantor trust means a trust in which a taxpayer is treated as owning an asset of the trust under subpart E of part I of subchapter J of chapter 1. (B) Beneficiary trust The term beneficiary trust means any trust that is not a grantor trust. (g) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including\u2014 (1) regulations establishing a process by which a beneficiary may demonstrate the portion of such beneficiary\u2019s interest in a trust, and (2) regulations for determining the appropriate attribution of assets in a trust for purposes of subsection (e)(1) in the case of a trust with multiple grantors. 2902. Net value of taxable assets (a) In general For purposes of this subtitle, the term net value of all taxable assets means, as of any date, the excess of\u2014 (1) the value of all property of the taxpayer (other than property excluded under subsection (b)), real or personal, tangible or intangible, wherever situated, over (2) any debts (including any debts secured by property excluded under subsection (b)) owed by the taxpayer. (b) Exclusion for certain assets under $50,000 Property of the taxpayer shall not be taken into account under subsection (a) if such property\u2014 (1) has a value of $50,000 or less (determined without regard to any debt owed by the taxpayer with respect to such property), (2) is tangible personal property, and (3) is not property\u2014 (A) which is used in a trade or business of the taxpayer, (B) in connection with which a deduction is allowable under section 212, or (C) which is a collectible as defined in section 408(m), a boat, an aircraft, a mobile home, a trailer, a vehicle, or an antique or other asset that maintains or increases its value over time (within the meaning of section 5.02(2) of Revenue Procedure 2018\u201308). (c) Rules for determining property of the taxpayer For purposes of this subtitle: (1) Property included in estate Any property that would be included in the estate of the taxpayer if the taxpayer died shall be treated as property of the taxpayer. (2) Inclusion of certain gifts Any property transferred by the taxpayer after the date of the enactment of this chapter, to an individual who is a member of the family of the taxpayer (as determined under section 267(c)(4)) and has not attained the age of 18 shall be treated as property of the taxpayer for any calendar year before the year in which such individual attains the age of 18. (d) Establishment of valuation rules Not later than 12 months after the date of the enactment of this section, the Secretary shall establish rules and methods for determining the value of any asset for purposes of this subtitle, including rules for the valuation of assets that are not publicly traded or that do not have a readily ascertainable value. Such rules and methods\u2014 (1) may utilize retrospective and prospective formulaic valuation methods not currently in use by the Secretary, (2) may require the use of formulaic valuation approaches for designated assets, including formulaic approaches based on proxies for determining presumptive valuations, formulaic approaches based on prospective adjustments from purchase prices or other prior events, or formulaic approaches based on retrospectively adding deferral charges based on eventual sale prices or other specified later events indicative of valuation, and (3) may address the use of valuation discounts. 2903. Special rules (a) Deceased individuals (1) In general In the case of any individual who dies during a calendar year and who is not married on the date of such individual's death\u2014 (A) section 2901 shall be applied by substituting the date of the applicable taxpayer's death for the last day of any calendar year , and (B) the amount of the tax imposed under such section shall be reduced by an amount which bears the same ratio to such amount (determined without regard to this subsection) as\u2014 (i) the number of days in the calendar year after the date of the individual's death, bears to (ii) 365. (2) Coordination with estate tax For purposes of section 2053, the tax imposed by this section for the year of the decedent's death shall be considered to have been imposed before such death. (b) Application to non-Residents In the case of any nonresident alien individual, this subtitle shall apply only to the property of such individual which is situated in the United States (determined under rules similar to the rules under subchapter B of chapter 11). (c) Application to covered expatriates In the case of an individual who is a covered expatriate (as defined in section 877A), section 2901(a) shall be applied as if the calendar year ended on the day before the expatriation. 2904. Information reporting (a) In general Not later than 12 months after the date of the enactment of this section, the Secretary shall by regulation require the reporting of any information concerning the net value of assets appropriate to enforce the tax imposed by this chapter. (b) Method of reporting The Secretary shall, where appropriate, require the reporting made under subsection (a) to be made as a part of existing income reporting requirements (including requirements under chapter 4 (relating to taxes to enforce reporting on certain foreign accounts)). (c) Responsibility for reporting The Secretary may impose reporting obligations by reference to the ownership, control, management, claim to income from, or other relationship to assets and liabilities for purposes of administering the tax imposed by this section and may impose such obligations on financial institutions, business entities, or other persons, including requiring business entities to provide estimates of the value of the entity itself. 2905. Enforcement The Secretary shall annually audit not less than 30 percent of taxpayers required to pay the tax imposed under this chapter. .\n##### (b) No deduction from income taxes\nSection 275 of such Code is amended by inserting after paragraph (6) the following new paragraph:\n(7) Taxes imposed by chapter 18. .\n##### (c) Extension of time for payment of tax\n**(1) In general**\nSection 6161(a) of such Code is amended by adding at the end the following new paragraph:\n(3) Wealth tax (A) In general In the case of an applicable taxpayer described in subparagraph (B), the Secretary may extend the time for payment of the tax imposed under chapter 18 for a reasonable period not to exceed 5 years from the date fixed for the payment thereof. (B) Taxpayers described An applicable taxpayer is described in this subparagraph if such the Secretary determines\u2014 (i) the applicable taxpayer has severe liquidity constraints, or (ii) immediate payment would cause undue hardship on an ongoing enterprise. (C) Applicable taxpayer For purposes of this paragraph, the term applicable taxpayer has the meaning given such term in section 2901. .\n**(2) Rules**\nNot later than 12 months after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall establish rules for the application of the amendments made by paragraph (1).\n##### (d) Application of accuracy related penalties\n**(1) In general**\nSection 6662(b) of such Code is amended by inserting after paragraph (10) the following new paragraph:\n(11) Any substantial wealth tax valuation understatement. .\n**(2) Substantial wealth tax understatement**\nSection 6662 of such Code is amended by adding at the end the following new subsection:\n(m) Application to substantial wealth tax valuation understatement (1) Substantial wealth tax valuation understatement defined (A) In general For purposes of this section, there is a substantial wealth tax valuation understatement if the value of any property claimed on any return of tax is 65 percent or less of the amount determined to be the correct amount of such valuation. (B) Limitation No penalty shall be imposed by reason of subsection (b)(11) unless the portion of the underpayment attributable to substantial wealth tax valuation understatements for the calendar year exceeds $5,000. (2) Increased penalty (A) In general In the case of any portion of an underpayment which is attributable to one or more substantial wealth tax valuation understatement, subsection (a) shall be applied\u2014 (i) in the case of a substantial wealth tax valuation understatement which is a gross wealth tax valuation misstatement, by substituting 50 percent for 20 percent , and (ii) in any other case, by substituting 30 percent for 20 percent . (B) Gross wealth tax valuation misstatement For purposes of subparagraph (A), the term gross wealth tax valuation misstatement means a substantial wealth tax valuation understatement, as determined under paragraph (1) by substituting 40 percent for 65 percent . .\n##### (e) Exemption of tax-Exempt entities\nSection 501(a) of such Code is amended by inserting and subtitle B\u20131 after this subtitle .\n##### (f) Clerical amendment\nThe table of subtitles of such Code is amended by inserting after the item relating to subtitle B the following new item:\nSubtitle B\u20131\u2014Wealth tax .\n##### (g) Effective date\nThe amendments made by this section shall apply to calendar years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-04-14",
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
        "name": "Taxation",
        "updateDate": "2025-05-12T19:37:43Z"
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
      "date": "2025-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2912ih.xml"
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
      "title": "Oligarch Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Oligarch Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a wealth tax, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:38Z"
    }
  ]
}
```
