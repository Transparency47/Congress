# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1798?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1798
- Title: End Tobacco Loopholes Act
- Congress: 119
- Bill type: HR
- Bill number: 1798
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-12-05T21:32:31Z
- Update date including text: 2025-12-05T21:32:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1798",
    "number": "1798",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "End Tobacco Loopholes Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:32:31Z",
    "updateDateIncludingText": "2025-12-05T21:32:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:04:10Z",
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "DC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1798ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1798\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Krishnamoorthi introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide tax rate parity among all tobacco products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Tobacco Loopholes Act .\n#### 2. Increasing excise taxes on cigarettes and establishing excise tax equity among all tobacco product tax rates\n##### (a) Tax parity for Roll-Your-Own tobacco\nSection 5701(g) of the Internal Revenue Code of 1986 is amended by striking $24.78 and inserting $49.56 .\n##### (b) Tax parity for pipe tobacco\nSection 5701(f) of the Internal Revenue Code of 1986 is amended by striking $2.8311 cents and inserting $49.56 .\n##### (c) Tax parity for smokeless tobacco\n**(1)**\nSection 5701(e) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin paragraph (1), by striking $1.51 and inserting $26.84 ;\n**(B)**\nin paragraph (2), by striking 50.33 cents and inserting $10.74 ; and\n**(C)**\nby adding at the end the following:\n(3) Smokeless tobacco sold in discrete single-use units On discrete single-use units, $100.66 per thousand. .\n**(2)**\nSection 5702(m) of such Code is amended\u2014\n**(A)**\nin paragraph (1), by striking or chewing tobacco and inserting , chewing tobacco, or discrete single-use unit ;\n**(B)**\nin paragraphs (2) and (3), by inserting that is not a discrete single-use unit before the period in each such paragraph; and\n**(C)**\nby adding at the end the following:\n(4) Discrete single-use unit The term discrete single-use unit means any product containing, made from, or derived from tobacco or nicotine that\u2014 (A) is not intended to be smoked; and (B) is in the form of a lozenge, tablet, pill, pouch, dissolvable strip, or other discrete single-use or single-dose unit. .\n##### (d) Tax parity for small cigars\nParagraph (1) of section 5701(a) of the Internal Revenue Code of 1986 is amended by striking $50.33 and inserting $100.66 .\n##### (e) Tax parity for large cigars\n**(1) In general**\nParagraph (2) of section 5701(a) of the Internal Revenue Code of 1986 is amended by striking 52.75 percent and all that follows through the period and inserting the following: $49.56 per pound and a proportionate tax at the like rate on all fractional parts of a pound but not less than 10.066 cents per cigar. .\n**(2) Guidance**\nThe Secretary of the Treasury, or the Secretary's delegate, may issue guidance regarding the appropriate method for determining the weight of large cigars for purposes of calculating the applicable tax under section 5701(a)(2) of the Internal Revenue Code of 1986.\n**(3) Conforming amendment**\nSection 5702 of such Code is amended by striking subsection (l).\n##### (f) Tax parity for Roll-Your-Own tobacco and certain processed tobacco\nSubsection (o) of section 5702 of the Internal Revenue Code of 1986 is amended by inserting , and includes processed tobacco that is removed for delivery or delivered to a person other than a person with a permit provided under section 5713, but does not include removals of processed tobacco for exportation after wrappers thereof .\n##### (g) Imposition of tax on nicotine for use in vaping, etc\n**(1) In general**\nSection 5701 of the Internal Revenue Code of 1986 is amended by redesignating subsection (h) as subsection (i) and by inserting after subsection (g) the following new subsection:\n(h) Nicotine On taxable nicotine, manufactured in or imported into the United States, there shall be imposed a tax equal to the dollar amount specified in section 5701(b)(1) per 1,810 milligrams of nicotine (and a proportionate tax at the like rate on any fractional part thereof). .\n**(2) Taxable nicotine**\nSection 5702 of such Code is amended by adding at the end the following new subsection:\n(q) Taxable nicotine (1) In general Except as otherwise provided in this subsection, the term taxable nicotine means any nicotine which has been extracted, concentrated, or synthesized. (2) Exception for products approved by Food and Drug Administration Such term shall not include any nicotine if the manufacturer or importer thereof demonstrates to the satisfaction of the Secretary of Health and Human Services that such nicotine will be used in\u2014 (A) a drug\u2014 (i) that is approved under section 505 of the Federal Food, Drug, and Cosmetic Act or licensed under section 351 of the Public Health Service Act; or (ii) for which an investigational use exemption has been authorized under section 505(i) of the Federal Food, Drug, and Cosmetic Act or under section 351(a) of the Public Health Service Act; or (B) a combination product (as described in section 503(g) of the Federal Food, Drug, and Cosmetic Act), the constituent parts of which were approved or cleared under section 505, 510(k), or 515 of such Act. (3) Coordination with taxation of other tobacco products Tobacco products meeting the definition of cigars, cigarettes, smokeless tobacco, pipe tobacco, and roll-your-own tobacco in this section shall be classified and taxed as such despite any concentration of the nicotine inherent in those products or any addition of nicotine to those products during the manufacturing process. (4) Regulations The Secretary shall prescribe such regulations or other guidance as is necessary or appropriate to carry out the purposes of this subsection, including regulations or other guidance for coordinating the taxation of tobacco products and taxable nicotine to protect revenue and prevent double taxation. .\n**(3) Taxable nicotine treated as a tobacco product**\nSection 5702(c) of such Code is amended by striking and roll-your-own tobacco and inserting roll-your-own tobacco, and taxable nicotine .\n**(4) Manufacturer of taxable nicotine**\nSection 5702 of such Code, as amended by paragraph (2), is amended by adding at the end the following new subsection:\n(r) Manufacturer of taxable nicotine (1) In general Any person who extracts, concentrates, or synthesizes nicotine shall be treated as a manufacturer of taxable nicotine (and as manufacturing such taxable nicotine). (2) Application of rules related to manufacturers of tobacco products Any reference to a manufacturer of tobacco products, or to manufacturing tobacco products, shall be treated as including a reference to a manufacturer of taxable nicotine, or to manufacturing taxable nicotine, respectively. .\n##### (h) Increasing tax on cigarettes\n**(1) Small cigarettes**\nSection 5701(b)(1) of such Code is amended by striking $50.33 and inserting $100.66 .\n**(2) Large cigarettes**\nSection 5701(b)(2) of such Code is amended by striking $105.69 and inserting $211.38 .\n##### (i) Tax rates adjusted for inflation\nSection 5701 of such Code, as amended by subsection (g), is amended by adding at the end the following new subsection:\n(j) Inflation adjustment (1) In general In the case of any calendar year beginning after 2026, the dollar amounts provided under this chapter shall each be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting \u2018calendar year 2025\u2019 for \u2018calendar year 2016\u2019 in subparagraph (A)(ii) thereof. (2) Rounding If any amount as adjusted under paragraph (1) is not a multiple of $0.01, such amount shall be rounded to the next highest multiple of $0.01. .\n##### (j) Floor Stocks Taxes\n**(1) Imposition of tax**\nOn tobacco products manufactured in or imported into the United States which are removed before any tax increase date and held on such date for sale by any person, there is hereby imposed a tax in an amount equal to the excess of\u2014\n**(A)**\nthe tax which would be imposed under section 5701 of the Internal Revenue Code of 1986 on the article if the article had been removed on such date, over\n**(B)**\nthe prior tax (if any) imposed under section 5701 of such Code on such article.\n**(2) Credit against tax**\nEach person shall be allowed as a credit against the taxes imposed by paragraph (1) an amount equal to $500. Such credit shall not exceed the amount of taxes imposed by paragraph (1) on such date for which such person is liable.\n**(3) Liability for tax and method of payment**\n**(A) Liability for tax**\nA person holding tobacco products on any tax increase date to which any tax imposed by paragraph (1) applies shall be liable for such tax.\n**(B) Method of payment**\nThe tax imposed by paragraph (1) shall be paid in such manner as the Secretary shall prescribe by regulations.\n**(C) Time for payment**\nThe tax imposed by paragraph (1) shall be paid on or before the date that is 120 days after the effective date of the tax rate increase.\n**(4) Articles in foreign trade zones**\nNotwithstanding the Act of June 18, 1934 (commonly known as the Foreign Trade Zone Act, 48 Stat. 998, 19 U.S.C. 81a et seq. ), or any other provision of law, any article which is located in a foreign trade zone on any tax increase date shall be subject to the tax imposed by paragraph (1) if\u2014\n**(A)**\ninternal revenue taxes have been determined, or customs duties liquidated, with respect to such article before such date pursuant to a request made under the first proviso of section 3(a) of such Act, or\n**(B)**\nsuch article is held on such date under the supervision of an officer of the United States Customs and Border Protection of the Department of Homeland Security pursuant to the second proviso of such section 3(a).\n**(5) Definitions**\nFor purposes of this subsection\u2014\n**(A) In general**\nAny term used in this subsection which is also used in section 5702 of such Code shall have the same meaning as such term has in such section.\n**(B) Tax increase date**\nThe term tax increase date means the effective date of any increase in any tobacco product excise tax rate pursuant to the amendments made by this section (other than subsection (j) thereof).\n**(C) Secretary**\nThe term Secretary means the Secretary of the Treasury or the Secretary\u2019s delegate.\n**(6) Controlled groups**\nRules similar to the rules of section 5061(e)(3) of such Code shall apply for purposes of this subsection.\n**(7) Other laws applicable**\nAll provisions of law, including penalties, applicable with respect to the taxes imposed by section 5701 of such Code shall, insofar as applicable and not inconsistent with the provisions of this subsection, apply to the floor stocks taxes imposed by paragraph (1), to the same extent as if such taxes were imposed by such section 5701. The Secretary may treat any person who bore the ultimate burden of the tax imposed by paragraph (1) as the person to whom a credit or refund under such provisions may be allowed or made.\n##### (k) Effective dates\n**(1) In general**\nExcept as provided in paragraphs (2) through (4), the amendments made by this section shall apply to articles removed (as defined in section 5702(j) of the Internal Revenue Code of 1986) after the last day of the month which includes the date of the enactment of this Act.\n**(2) Discrete single-use units and processed tobacco**\nThe amendments made by subsections (c)(1)(C), (c)(2), and (f) shall apply to articles removed (as defined in section 5702(j) of the Internal Revenue Code of 1986) after the date that is 6 months after the date of the enactment of this Act.\n**(3) Large cigars**\nThe amendments made by subsection (e) shall apply to articles removed after December 31, 2025.\n**(4) Taxable nicotine**\nThe amendments made by subsection (g) shall apply to articles removed in calendar quarters beginning after the date which is 180 days after the date of the enactment of this Act.\n##### (l) Transition rule for permit and bond requirements\nA person which is lawfully engaged in business as a manufacturer or importer of taxable nicotine (within the meaning of subchapter A of chapter 52 of the Internal Revenue Code of 1986, as amended by this section) on the date of the enactment of this Act, first becomes subject to the requirements of subchapter B of chapter 52 of such Code by reason of the amendments made by this section, and submits an application under such subchapter B to engage in such business not later than 90 days after the date of the enactment of this Act, shall not be denied the right to carry on such business by reason of such requirements before final action on such application.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-03-03",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S1462-1463)"
      },
      "number": "819",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Tobacco Loopholes Act",
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
        "updateDate": "2025-05-07T14:15:38Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1798ih.xml"
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
      "title": "End Tobacco Loopholes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Tobacco Loopholes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide tax rate parity among all tobacco products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T02:48:18Z"
    }
  ]
}
```
