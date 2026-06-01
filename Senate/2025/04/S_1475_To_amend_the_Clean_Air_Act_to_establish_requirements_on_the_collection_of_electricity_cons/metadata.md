# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1475?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1475
- Title: Clean Cloud Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1475
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-01-27T15:09:00Z
- Update date including text: 2026-01-27T15:09:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1475",
    "number": "1475",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Clean Cloud Act of 2025",
    "type": "S",
    "updateDate": "2026-01-27T15:09:00Z",
    "updateDateIncludingText": "2026-01-27T15:09:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T20:30:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1475is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1475\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Whitehouse (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to establish requirements on the collection of electricity consumption data and emissions standards for servers and other computing equipment used for cryptocurrency mining, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Cloud Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\ndata centers are estimated to account for approximately\u2014\n**(A)**\n1 percent of global electricity demand; and\n**(B)**\n4 percent of United States electricity use;\n**(2)**\nthe growing demand for information technology and artificial intelligence will increase the demand for data center services;\n**(3)**\nthe global COVID\u201319 pandemic has further increased the demand described in paragraph (2) beyond previous projections;\n**(4)**\ndata centers are projected to account for up to 12 percent of United States electricity use by 2028;\n**(5)**\nfuture electricity consumption and efficiency trends will be determined by management practices, demand for services, and adoption of efficient technologies;\n**(6)**\nproof-of-work cryptocurrencies are by design an increasingly energy intensive process;\n**(7)**\nstudies estimate that\u2014\n**(A)**\nthe total network hashrate for Bitcoin mining in the United States has increased 739 percent between September 2020 and January 2022; and\n**(B)**\nas of July 2021, the greatest share of Bitcoin mining occurs in the United States;\n**(8)**\nthere is a lack of transparency regarding the energy sources used to power domestic cryptomining and many data center operations; and\n**(9)**\nretired and retiring fossil fuel plants in the United States are being brought back online to power cryptomining facilities and data centers, which increases associated carbon emissions.\n#### 3. Emissions from power consumption of data centers and cryptomining facilities\nPart A of title I of the Clean Air Act ( 42 U.S.C. 7401 et seq. ) is amended by adding at the end the following:\n139. Emissions from power consumption of data centers and cryptomining facilities (a) Definitions In this section: (1) Covered facility The term covered facility means a data center or cryptomining facility that has more than 100 kilowatts of installed information technology nameplate power. (2) Cryptomining facility The term cryptomining facility means a facility used to mine or create cryptocurrencies or other blockchain based digital assets, which may be\u2014 (A) a freestanding structure; or (B) a facility within a larger structure that uses environmental control equipment to maintain the proper conditions for the operation of electronic equipment. (3) Data center The term data center has the meaning given the term in section 453(a) of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17112(a) ). (4) Electric utility The term electric utility has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ). (5) Region The term region means a geographic region described in the National Transmission Needs Study of the Department of Energy, dated October 30, 2023. (b) Annual data collection of energy consumption of data centers and cryptomining facilities (1) In general The Administrator, in conjunction with the Administrator of the Energy Information Administration, shall annually collect\u2014 (A) the information described in paragraph (2) from the owners of covered facilities, including federally owned data centers located within the United States and territories of the United States; and (B) the information described in paragraph (3) from the electric utilities that serve covered facilities. (2) Information described for covered facilities The information referred to in paragraph (1)(A), with respect to a covered facility, is\u2014 (A) the location of the covered facility, including in which balancing authority area the covered facility is located; (B) whether the covered facility is a data center or a cryptomining facility; (C) the owner of the covered facility; (D) the electric utility, if any, that provides power to the covered facility; (E) the total annual electricity consumption of the covered facility; (F) the total annual electricity consumed by the covered facility from electricity generation assets located behind the power meter of the covered facility; (G) subject to paragraph (5), the percentage of electricity consumed annually by the covered facility from electricity generation assets located behind the power meter of the covered facility that is generated from wind, solar, hydropower, nuclear, coal, gas, and any other power source; (H) the terms of any power purchase agreements or other contractual mechanisms for procuring power from an electricity generator that the covered facility is party to; and (I) any other relevant information, as reasonably determined by the Administrator and the Administrator of the Energy Information Administration. (3) Information described for electric utilities The information referred to in paragraph (1)(B), with respect to each covered facility served by an electric utility, is\u2014 (A) the total annual electricity consumed by the covered facility from the electric grid; (B) subject to paragraph (4), the percentage of electricity consumed annually by the covered facility from the electric grid that is generated from wind, solar, hydropower, nuclear, coal, gas, and any other power source; (C) the rates charged by the electric utility for each class of electric consumer for the current year and each of the 3 prior years; and (D) any other relevant information, as reasonably determined by the Administrator and the Administrator of the Energy Information Administration. (4) Electricity consumed from the electric grid For purposes of collecting the information described in paragraph (3)(B) with respect to a covered facility\u2014 (A) the Administrator, in conjunction with the Administrator of the Energy Information Administration, shall consider the average resource mix of the electric utilities that serve the covered facility to be the resource mix for the portion of electricity consumed annually from the electric grid by a covered facility that is not described in subparagraph (B); and (B) if the covered facility or the owner of the covered facility is party to a power purchase agreement or other contractual mechanism for procuring power from an electricity generation asset (such as the voluntary higher rate described in subsection (c)(4)(C)(iii)(I)(aa)), or purchases and retires energy attribute certificates, the Administrator, in conjunction with the Administrator of the Energy Information Administration, shall consider the electricity generation represented by those instruments as part of the electricity consumed annually by the covered facility from the electric grid only if the owner of the covered facility can demonstrate that\u2014 (i) (I) the electricity generation asset began commercial operations not more than 36 months before the date on which operations began at the covered facility; (II) the electricity generation asset would otherwise be retired and the retirement could not be prevented by the use of existing public funding programs; (III) the electricity provided by the electricity generation asset would otherwise be curtailed; (IV) the power that the electricity generation asset provides to the covered facility resulted from an uprate that occurred not more than 36 months before the date on which operations began at the covered facility; (V) the power purchase agreement or other contractual mechanism was finalized before the date of enactment of this section; or (VI) (aa) the electricity generation asset has undergone or will undergo a retrofit that reduces the greenhouse emissions intensity of the electricity generation asset, expressed in terms of metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour, by not less than 75 percent, as compared to before the retrofit; and (bb) the retrofit otherwise would not have occurred, even after the use of existing public funding programs, without the power purchase agreement or other contractual mechanism; (ii) the electricity is generated\u2014 (I) in the same calendar year as the electricity is consumed by the covered facility, in the case of electricity that is generated before January 1, 2028; and (II) in the same hour as the electricity is consumed by the covered facility or an energy storage asset that serves the covered facility, in the case of electricity that is generated after December 31, 2027; (iii) (I) the electricity generation asset that produced the electricity is electrically interconnected to a balancing authority located in the same region as the covered facility; or (II) the owner of the electricity generation asset can demonstrate that the power produced by the electricity generation asset is physically delivered to the covered facility, as determined by the Administrator, in coordination with the Secretary of Energy; and (iv) the electricity generation represented by the power purchase agreement or other contractual mechanism for procuring power from an electricity generation asset are claimed exclusively by the covered facility through the retirement of an equivalent quantity of energy attribute certificates. (5) Electricity consumed from assets behind the meter For purposes of collecting the information described in paragraph (2)(G) with respect to a covered facility\u2014 (A) the Administrator, in conjunction with the Administrator of the Energy Information Administration, shall consider the average resource mix of the electric utilities that serve the covered facility to be the resource mix for the portion of electricity consumed annually by the covered facility from electricity generation assets located behind the power meter of a covered facility that is not described in subparagraph (B); and (B) the Administrator, in conjunction with the Administrator of the Energy Information Administration, shall consider the electricity generated by electricity generation assets located behind the power meter of the covered facility as part of the electricity consumed annually by the covered facility from electricity generation assets located behind the power meter of the covered facility only if\u2014 (i) the owner of the covered facility can demonstrate that\u2014 (I) the electricity generation asset began operations not more than 36 months before the date on which operations began at the covered facility; or (II) the electricity generation asset would otherwise be retired and the retirement could not be prevented by the use of existing public funding programs; or (ii) the Administrator determines that the greenhouse gas emissions intensity, expressed in terms of metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour, of the electricity generation asset is higher than the greenhouse gas emissions intensity of the electric utilities that serve the covered facility, based on the average resource mix of those electric utilities. (6) Greenhouse gas emissions intensity Based on the information collected under paragraph (1), for each covered facility, the Administrator shall determine the greenhouse gas emission intensity, expressed in terms of metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour, of\u2014 (A) the total annual electricity consumed by the covered facility from the electric grid; and (B) the total annual electricity consumed by the covered facility from electricity generation assets located behind the power meter of the covered facility. (7) Publicly available The Administrator shall make publicly available on an annual basis\u2014 (A) for each covered facility\u2014 (i) the information described in each of subparagraphs (A), (B), (C), and (D) of paragraph (2); (ii) the percent of electricity consumed annually by the covered facility that is generated from wind, solar, hydropower, nuclear, coal, gas, and any other power source; and (iii) the greenhouse gas emissions intensity of the total annual electricity consumed by the covered facility, as determined under paragraph (6); and (B) for each owner of a covered facility, the aggregate annual electricity consumption of all covered facilities owned by that owner. (8) Confidential business information (A) In general Except as provided in subparagraph (B), of the information collected under paragraph (1), the Administrator and the Administrator of the Energy Information Administration shall treat the information described in each of subparagraphs (E) and (F) of paragraph (2) and subparagraph (A) of paragraph (3) as confidential business information. (B) Exception Subparagraph (A) does not apply to information that is required to be made publicly available pursuant to paragraph (7)(C). (c) Emissions performance standard (1) Definitions In this subsection: (A) Baseline The term baseline , with respect to a covered facility in a calendar year, means the baseline of the region the covered facility is located in for that calendar year as determined under paragraph (2). (B) Greenhouse gas (i) In general The term greenhouse gas means the air pollutants carbon dioxide, any hydrofluorocarbon, methane, nitrous oxide, any perfluorocarbon, and sulfur hexafluoride. (ii) Global warming potential For purposes of the term methane in clause (i), the Administrator shall use the 20-year global warming potential of methane, as determined in accordance with the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. (2) Determination of baseline (A) Publication of baseline Not later than December 31, 2025, the Administrator shall determine and publish in the Federal Register the greenhouse gas emissions intensities of the electric grid of each region, expressed in terms of metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour. (B) Initial baseline For purposes of calendar year 2026, the baseline of each region shall be the baseline of that region published under subparagraph (A). (C) Baselines through 2034 For each of calendar years 2027 through 2034, the baseline of each region for that calendar year shall be determined by reducing the baseline from the previous calendar year by 11 percent of the baseline of that region for calendar year 2026. (D) Baseline in 2035 and thereafter For calendar year 2035 and each calendar year thereafter, the baseline for each region shall be 0 metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour. (3) Assessment of fees (A) Fee on utilities (i) Imposition of fee on utilities Beginning on January 1, 2026, the Administrator shall, in accordance with this subparagraph and using the information collected under subsection (b) but subject to subparagraphs (C) and (D), assess on the owner of any electric utility providing power to a covered facility a fee with respect to the greenhouse gas emissions of the electricity consumed by the covered facility from the electric grid above the baseline of the region the covered facility is located in for that calendar year. (ii) Amount of fee The amount of a fee assessed under clause (i) with respect to an electric utility for a calendar year shall be the sum obtained by adding, for each covered facility served by the electric utility, the product (rounded to the nearest dollar) obtained by multiplying\u2014 (I) the total electricity consumed by the covered facility from the electric grid during the calendar year, as expressed in kilowatt-hours; (II) subject to clause (iii), $20; and (III) the amount, if any, that the greenhouse gas emissions intensity of the electricity consumed by the covered facility from the electric grid, expressed in terms of metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour, exceeds the baseline of the region the covered facility is located in for the calendar year. (iii) Fee adjustment Beginning in calendar year 2027, the Administrator shall annually increase the amount described in clause (ii)(II) by the sum obtained by adding\u2014 (I) the product obtained by multiplying\u2014 (aa) the applicable amount under clause (ii)(II) during the previous calendar year; and (bb) the rate of inflation, as determined by the Administrator using the changes for the 12-month period ending the preceding November 30 in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor; and (II) $10. (iv) Notification of fee amount Not later than January 31, 2027, and not later than January 31 of each calendar year thereafter, the Administrator shall notify\u2014 (I) the owner of each electric utility subject to a fee under clause (i) of the amount of the fee that is assessed with respect to the electric utility for the previous calendar year under clause (i); and (II) the owner of each covered facility of the total amount of any fee assessed for the previous calendar year under clause (i) that is attributable, pursuant to clause (ii), to the electricity consumed by the covered facility. (v) Remittance of fee amount A fee assessed under clause (i) for a calendar year shall be due and payable to the Administrator not later than March 31 of the calendar year after the calendar year for which the fee is assessed. (vi) Pass-through limitation (I) In general Any electric utility assessed a fee under clause (i) may not recoup the cost of the fee by raising rates or assessing fees on any customer that is not a covered facility. (II) Monitoring compliance The Administrator, in conjunction with the Administrator of the Energy Information Administration, shall use the best available data, including the information collected pursuant to subsection (b)(1)(B) and described in subsection (b)(3)(C), to monitor the compliance of electric utilities with subclause (I). (III) Penalty If the Administrator, in conjunction with the Administrator of the Energy Information Administration, determines that an electric utility has violated subclause (I), the Administrator shall assess a fine on the electric utility in an amount equal to 2 times the amount recouped by the electric utility, as described in subclause (I), from customers that are not covered facilities. (B) Fee on covered facilities (i) Imposition of fee on covered facilities Beginning on January 1, 2026, the Administrator shall, in accordance with this subparagraph and using the information collected under subsection (b) but subject to subparagraphs (C) and (D), assess on the owner of any covered facility a fee with respect to the greenhouse gas emissions of the electricity consumed by the covered facility from electricity generation assets located behind the power meter of the covered facility above the baseline of the region the covered facility is located in for that calendar year. (ii) Amount of fee The amount of a fee assessed under clause (i) with respect to a covered facility for a calendar year shall be the product (rounded to the nearest dollar) obtained by multiplying\u2014 (I) the total electricity consumed by the covered facility from electricity generation assets located behind the power meter of the covered facility during the calendar year, as expressed in kilowatt-hours; (II) subject to clause (iii), $20; and (III) the amount, if any, that the greenhouse gas emissions intensity of the electricity consumed by the covered facility from electricity generation assets located behind the power meter of the covered facility, expressed in terms of metric tons of carbon dioxide-equivalent of greenhouse gases per kilowatt-hour, exceeds the baseline of the region the covered facility is located in for the calendar year. (iii) Fee adjustment Beginning in calendar year 2027, the Administrator shall annually increase the amount described in clause (ii)(II) by the sum obtained by adding\u2014 (I) the product obtained by multiplying\u2014 (aa) the applicable amount under clause (ii)(II) during the previous calendar year; and (bb) the rate of inflation, as determined by the Administrator using the changes for the 12-month period ending the preceding November 30 in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor; and (II) $10. (iv) Notification of fee amount Not later than January 31, 2027, and not later than January 31 of each calendar year thereafter, the Administrator shall notify the owner of each covered facility the amount of the fee that is assessed with respect to the covered facility for the previous calendar year under clause (i). (v) Remittance of fee amount A fee assessed under clause (i) for a calendar year shall be due and payable to the Administrator not later than March 31 of the calendar year after the calendar year for which the fee is assessed. (C) Applicability to zero-carbon electricity generation assets This paragraph shall not apply to a covered facility if the Administrator, in conjunction with the Administrator of the Energy Information Administration, determines, pursuant to the information collected under subsection (b), that the covered facility is powered entirely by zero-carbon electricity generation assets during all hours of the operation of the covered facility. (D) Alternative baseline If the Administrator determines at any point that the greenhouse gas emissions intensity of the electric grid of any region falls below the baseline of that region, during the period beginning on the date of that determination and ending on the date on which the Administrator determines that the determination is no longer applicable, subparagraphs (A) and (B) shall be applied to covered facilities located in that region by substituting greenhouse gas emissions intensity of the electric grid for baseline . (4) Use of funds (A) Administration For fiscal year 2028 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Administrator an amount equal to 3 percent of the amounts collected pursuant to fees and penalties assessed under paragraph (3) during the previous calendar year to support the administration of the reporting program under subsection (b) and the assessment of the fees and penalties under this subsection. (B) Consumer energy costs For fiscal year 2028 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Administrator an amount equal to 25 percent of the amounts collected pursuant to fees and penalties assessed under paragraph (3) during the previous calendar year to award grants to States, Indian Tribes, municipalities, and electric utilities to support programs that lower residential electricity consumer energy costs, such as through energy use savings or direct rebates, to offset cost increases resulting from increased data center electricity consumption. (C) Clean firm grants (i) In general For fiscal year 2028 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Administrator an amount equal to 70 percent of the amounts collected pursuant to fees and penalties assessed under paragraph (3) during the previous calendar year to award to eligible entities, as determined by the Administrator, grants, rebates, advanced market commitments, or low-interest loans, as determined appropriate by the Administrator, for the research, development, demonstration, and deployment of\u2014 (I) zero-carbon electricity generation assets that are capable of generating electricity throughout the year, with the exception of planned outages for maintenance, refueling, or retrofits, at capacity factors greater than 70 percent; or (II) long-duration energy storage assets that are capable of continuously discharging energy at their rated power output for at least 10 hours. (ii) Application An eligible entity seeking an award under clause (i) shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require. (iii) Certification and clawback (I) Certification An eligible entity that receives an award under clause (i) for the purpose of financing the construction or operation of an electricity generation asset or energy storage asset shall certify that any electric utility selling or contracted to sell electricity generated or stored by the asset shall\u2014 (aa) not later than 2 years after the date on which the eligible entity receives the award, allow the customers of the electric utility to voluntarily pay a higher rate for the purchase of electricity service that is sourced from zero-carbon electricity generation, including long-duration energy storage assets charged by zero-carbon electricity, in all hours of the year; and (bb) exclusively use the additional amounts collected pursuant to those higher rates to support the financing, development, or acquisition of\u2014 (AA) zero-carbon electricity generation assets that are capable of generating electricity throughout the year, with the exception of planned outages for maintenance, refueling, or retrofits, at capacity factors greater than 70 percent; or (BB) long-duration energy storage assets that are capable of continuously discharging energy at their rated power output for at least 10 hours. (II) Clawback If the Administrator determines that a recipient of an award described in subclause (I) has violated the certification required under that subclause, the Administrator shall seek reimbursement of the full amount of the award from the recipient. (d) Applicability to leased facilities For purposes of this section\u2014 (1) if a covered facility is leased to a tenant, the tenant shall be considered the owner of the facility; and (2) if a portion of a covered facility is leased to a tenant and the leased space also meets the requirements described in subsection (a)(1)\u2014 (A) the leased space shall be considered to be a separate covered facility from the rest of the larger facility; and (B) the tenant shall be considered the owner of the covered facility that comprises the leased space. .\n#### 4. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act and the amendments made by this Act, and the application of the provision or amendment to any other person or circumstance, shall not be affected by the holding.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6179",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Clean Cloud Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-20T12:32:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1475",
          "measure-number": "1475",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-01-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1475v00",
            "update-date": "2026-01-27"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Clean Cloud Act of 2025</strong></p><p>This bill establishes an emissions standard and fee system regarding the electricity used by data centers or\u00a0cryptomining facilities that exceed a specified size.\u00a0Additionally, the bill appropriates collected fees for various purposes, including to fund zero-carbon electricity generation, long-duration energy storage, and grants to lower residential electricity consumer costs.</p><p>The bill requires the Environmental Protection Agency (EPA) and the Energy Information Administration to annually determine the greenhouse gas emission intensity of the total annual electricity consumed by (1) covered facilities from the electric grid,\u00a0and (2) covered facilities from electricity generation assets located\u00a0behind the power meter of the facilities.</p><p>The EPA must determine and publish the greenhouse gas emissions intensities of the electric grid of each region to establish a baseline for the assessment of fees. Each calendar year from 2027 through 2034, the baseline for each region is reduced by 11% of the original\u00a0baseline. For 2035 and after, the baseline is set to zero emissions.</p><p>The EPA must assess a fee on (1) owners of any electric utility providing power to a covered facility that exceeds the baseline emissions in that region for that year, and (2) covered facilities with respect to the greenhouse gas emissions from electricity generation assets located behind the power meter of the facility above the baseline of the region for that year. The electric utilities may not recoup the cost of the fee by raising rates or assessing fees on customers that are not covered facilities.</p>"
        },
        "title": "Clean Cloud Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1475.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Clean Cloud Act of 2025</strong></p><p>This bill establishes an emissions standard and fee system regarding the electricity used by data centers or\u00a0cryptomining facilities that exceed a specified size.\u00a0Additionally, the bill appropriates collected fees for various purposes, including to fund zero-carbon electricity generation, long-duration energy storage, and grants to lower residential electricity consumer costs.</p><p>The bill requires the Environmental Protection Agency (EPA) and the Energy Information Administration to annually determine the greenhouse gas emission intensity of the total annual electricity consumed by (1) covered facilities from the electric grid,\u00a0and (2) covered facilities from electricity generation assets located\u00a0behind the power meter of the facilities.</p><p>The EPA must determine and publish the greenhouse gas emissions intensities of the electric grid of each region to establish a baseline for the assessment of fees. Each calendar year from 2027 through 2034, the baseline for each region is reduced by 11% of the original\u00a0baseline. For 2035 and after, the baseline is set to zero emissions.</p><p>The EPA must assess a fee on (1) owners of any electric utility providing power to a covered facility that exceeds the baseline emissions in that region for that year, and (2) covered facilities with respect to the greenhouse gas emissions from electricity generation assets located behind the power meter of the facility above the baseline of the region for that year. The electric utilities may not recoup the cost of the fee by raising rates or assessing fees on customers that are not covered facilities.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119s1475"
    },
    "title": "Clean Cloud Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Clean Cloud Act of 2025</strong></p><p>This bill establishes an emissions standard and fee system regarding the electricity used by data centers or\u00a0cryptomining facilities that exceed a specified size.\u00a0Additionally, the bill appropriates collected fees for various purposes, including to fund zero-carbon electricity generation, long-duration energy storage, and grants to lower residential electricity consumer costs.</p><p>The bill requires the Environmental Protection Agency (EPA) and the Energy Information Administration to annually determine the greenhouse gas emission intensity of the total annual electricity consumed by (1) covered facilities from the electric grid,\u00a0and (2) covered facilities from electricity generation assets located\u00a0behind the power meter of the facilities.</p><p>The EPA must determine and publish the greenhouse gas emissions intensities of the electric grid of each region to establish a baseline for the assessment of fees. Each calendar year from 2027 through 2034, the baseline for each region is reduced by 11% of the original\u00a0baseline. For 2035 and after, the baseline is set to zero emissions.</p><p>The EPA must assess a fee on (1) owners of any electric utility providing power to a covered facility that exceeds the baseline emissions in that region for that year, and (2) covered facilities with respect to the greenhouse gas emissions from electricity generation assets located behind the power meter of the facility above the baseline of the region for that year. The electric utilities may not recoup the cost of the fee by raising rates or assessing fees on customers that are not covered facilities.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119s1475"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1475is.xml"
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
      "title": "Clean Cloud Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Clean Cloud Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to establish requirements on the collection of electricity consumption data and emissions standards for servers and other computing equipment used for cryptocurrency mining, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:21Z"
    }
  ]
}
```
