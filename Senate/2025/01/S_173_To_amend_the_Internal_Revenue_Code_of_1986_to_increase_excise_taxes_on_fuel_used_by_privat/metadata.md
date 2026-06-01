# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/173?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/173
- Title: Fueling Alternative Transportation with a Carbon Aviation Tax Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 173
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2025-05-27T14:12:54Z
- Update date including text: 2025-05-27T14:12:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/173",
    "number": "173",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Fueling Alternative Transportation with a Carbon Aviation Tax Act of 2025",
    "type": "S",
    "updateDate": "2025-05-27T14:12:54Z",
    "updateDateIncludingText": "2025-05-27T14:12:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T22:41:31Z",
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
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-21",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s173is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 173\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Markey (for himself, Mr. Murphy , Mr. Merkley , Mr. Sanders , Ms. Warren , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase excise taxes on fuel used by private jets, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fueling Alternative Transportation with a Carbon Aviation Tax Act of 2025 .\n#### 2. Increase in excise tax for fuel used by private jets\n##### (a) In general\n**(1) Retail excise tax**\nSection 4041(c) of the Internal Revenue Code of 1986 is amended by striking paragraph (3) and inserting the following:\n(3) Rate of tax The rate of tax imposed by this subsection shall be\u2014 (A) with respect to any sale or use for commercial aviation, 4.3 cents per gallon, and (B) with respect to any sale or use which is not described in subparagraph (A), an amount equal to the sum of\u2014 (i) 35.9 cents per gallon, plus (ii) $1.641 per gallon. (4) Inflation adjustment In the case of any calendar year beginning after 2026, the dollar amount in paragraph (3)(B)(ii) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. .\n**(2) Manufacturers excise tax**\nSection 4081(a)(2) of such Code is amended\u2014\n**(A)**\nin subparagraph (C), by striking clause (ii) and inserting the following:\n(ii) in the case of use for aviation not described in clause (i), an amount equal to the sum of\u2014 (I) 35.9 cents per gallon, plus (II) $1.641 per gallon. , and\n**(B)**\nby adding at the end the following:\n(E) Inflation adjustment In the case of any calendar year beginning after 2026, the dollar amount in subparagraph (C)(ii)(II) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. .\n**(3) Conforming amendments**\n**(A)**\nSection 4081(d)(2) of such Code is amended by striking (a)(2)(C)(ii) and inserting (a)(2)(C)(ii)(I) .\n**(B)**\nSection 6427(l)(4)(B)(ii)(II) of such Code is amended by striking section 4081(a)(2)(C)(ii) and inserting section 4081(a)(2)(C)(ii)(I) .\n**(C)**\nSection 9503(c)(5)(B) of such Code is amended by striking 21.8 cents and inserting 35.9 cents .\n##### (b) Refund or credit in cases of reasonable cause\nSection 6427 of the Internal Revenue Code of 1986 is amended by inserting after subsection (e) the following new subsection:\n(f) Exception from increase in rate of tax for certain liquids used as fuel in non-Commercial aviation (1) Retail excise tax Except as provided in subsection (k), in the case of any fuel on the sale of which tax was imposed under section 4041(c) for which the rate of tax was determined under paragraph (3)(B) of such section, if the Secretary determines (pursuant to such regulations as are prescribed by the Secretary) that there is reasonable cause that the increase in the rate of tax pursuant to clause (ii) of such paragraph should not apply with respect to such fuel (such as in cases where the fuel was used in an aircraft which was engaged in scientific research, an evacuation from a natural disaster, or assistance in a medical emergency), the Secretary shall pay (without interest) to the ultimate purchaser of such fuel an amount equal to the increase in the amount of the tax imposed on such fuel pursuant to such clause. (2) Manufacturers excise tax Except as provided in subsection (k), in the case of any kerosene on which tax was imposed under section 4081 for which the rate of tax was determined under subsection (a)(2)(C)(ii) of such section, if the Secretary determines (pursuant to such regulations as are prescribed by the Secretary) that there is reasonable cause that the increase in the rate of tax pursuant to subclause (II) of such subsection should not apply with respect to such kerosene (such as in cases where the kerosene was used in an aircraft which was engaged in scientific research, an evacuation from a natural disaster, or assistance in a medical emergency), the Secretary shall pay (without interest) to the ultimate purchaser of such kerosene an amount equal to the increase in the amount of the tax imposed on such kerosene pursuant to such subclause. (3) Termination This subsection shall not apply to any fuel sold or used after January 1, 2028. .\n##### (c) Elimination of exemption from air transportation excise tax\nSection 4261(f) of the Internal Revenue Code of 1986 is amended to read as follows:\n(f) Exemption for certain uses (1) In general No tax shall be imposed under subsection (a) or (b) on air transportation by helicopter or by fixed-wing aircraft for the purpose of the planting, cultivation, cutting, or transportation of, or caring for, trees. (2) Requirement Paragraph (1) shall apply only if the helicopter or fixed-wing aircraft does not take off from, or land at, a facility eligible for assistance under the Airport and Airway Development Act of 1970, or otherwise use services provided pursuant to section 44509 or 44913(b) or subchapter I of chapter 471 of title 49, United States Code, during such use. .\n##### (d) Effective date\nThe amendments made by this section shall take effect on January 1, 2026.\n#### 3. Funding to Support Clean Communities Trust Fund\n##### (a) In general\nSubchapter A of chapter 98 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9512. Funding to Support Clean Communities Trust Fund (a) Establishment and funding There is hereby established in the Treasury of the United States a trust fund to be referred to as the \u2018Funding to Support Clean Communities Trust Fund\u2019, consisting of such amounts as may be appropriated or credited to such trust fund as provided for in this section and section 9602(b). (b) Transfers to Trust Fund There are hereby appropriated to the Funding to Support Clean Communities Trust Fund amounts equivalent to the taxes received in the Treasury under\u2014 (1) section 4041(c) to the extent attributable to the rate specified in paragraph (3)(B)(ii) of such section, and (2) section 4081 with respect to kerosene to the extent attributable to the rate specified in section 4081(a)(2)(C)(ii)(II). (c) Expenditures from Trust Fund (1) In general Subject to paragraph (2), amounts in the Funding to Support Clean Communities Trust Fund shall be available, as provided by appropriation Acts, for making expenditures for grants and other activities\u2014 (A) authorized under subsections (a) through (c) of section 103 and section 105 of the Clean Air Act ( 42 U.S.C. 7403(a) \u2013(c), 7405), including grants and other activities to\u2014 (i) deploy, integrate, support, and maintain fenceline air monitoring, screening air monitoring, national air toxics trend stations, and other air toxics and community monitoring, (ii) expand the national ambient air quality monitoring network with new multipollutant monitoring stations, (iii) replace, repair, operate, and maintain existing monitors, and (iv) deploy, integrate, and operate air quality sensors in low-income and disadvantaged communities, (B) to expand, connect, replace, repair, operate, and maintain public transit and passenger rail infrastructure or systems that are located 20 miles or less from an airport, and (C) to improve public transportation, particularly in disadvantaged communities, including costs associated with efforts to provide more safe, frequent, and reliable bus service. (2) Set aside for disadvantaged communities (A) In general For any calendar year, not less than 50 percent of the amounts made available under paragraph (1) shall be designated for expenditures for grants and other activities within disadvantaged communities. (B) Prioritization of funds for communities disproportionally impacted by air pollution With respect to making expenditures for grants and other activities described in paragraph (1) to disadvantaged communities, priority shall be given to communities that are disproportionately impacted by air pollution (as determined by the Secretary in consultation with the Administrator of the Environmental Protection Agency). (d) Disadvantaged community For purposes of this section\u2014 (1) In general The term disadvantaged community means a community with significant representation of low-income communities or socially disadvantaged groups (as defined in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) )) that experiences or is at risk of experiencing higher or more adverse human health or environmental effects. (2) Low-income community For purposes of paragraph (1), the term low-income community means any census block group in which 30 percent or more of the population are individuals with an annual household income equal to, or less than, the greater of\u2014 (A) an amount equal to 80 percent of the median income of the area in which the household is located, as reported by the Department of Housing and Urban Development, and (B) 200 percent of the Federal poverty line. .\n##### (b) Conforming amendments to Airport and Airway Trust Fund\nSection 9502(b)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subparagraph (A), by inserting to the extent attributable to the rates specified in subparagraphs (A) and (B)(i) of section 4041(c)(3), after (relating to aviation fuels), , and\n**(2)**\nin subparagraph (D), by striking rate specified in and inserting rates specified in clauses (i) and (ii)(I) of .\n##### (c) Clerical amendment\nThe table of sections for subchapter A of chapter 98 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9512. Funding to Support Clean Communities Trust Fund. .\n##### (d) Effective date\nThe amendments made by this section shall take effect on January 1, 2026.",
      "versionDate": "2025-01-21",
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
        "updateDate": "2025-02-26T16:17:55Z"
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
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s173is.xml"
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
      "title": "Fueling Alternative Transportation with a Carbon Aviation Tax Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fueling Alternative Transportation with a Carbon Aviation Tax Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase excise taxes on fuel used by private jets, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:24Z"
    }
  ]
}
```
