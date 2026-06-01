# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2872?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2872
- Title: Emergency Pine Beetle Response Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2872
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-11-25T16:13:39Z
- Update date including text: 2025-11-25T16:13:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2872",
    "number": "2872",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Emergency Pine Beetle Response Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T16:13:39Z",
    "updateDateIncludingText": "2025-11-25T16:13:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T18:40:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "LA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2872is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2872\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mrs. Hyde-Smith (for herself, Mr. Ossoff , Mrs. Britt , Mr. Kennedy , Mr. Tuberville , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Credit Act of 1978 to authorize assistance for emergency measures in response to pine beetle outbreaks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Pine Beetle Response Act of 2025 .\n#### 2. Emergency measures in response to pine beetle outbreaks\nSection 407 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2206 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Emergency measures in response to pine beetle outbreaks (1) Definitions In this subsection: (A) Eligible itemized costs The term eligible itemized costs means any expenses incurred by a timber service business in carrying out a contractual service associated with an outbreak response measure, including\u2014 (i) labor or hours for truck drivers or equipment operators; (ii) mileage or hours for use of equipment, such as transports, bulldozers, and skidders; and (iii) materials, such as gravel, grass seed, culverts, mats, and insecticides. (B) Outbreak response measure The term outbreak response measure means any measure necessary to address a pine beetle outbreak on nonindustrial private forest land, including\u2014 (i) timber harvesting or thinning; (ii) prescribed burning; (iii) debris removal; (iv) insecticide treatment; (v) establishment of buffer areas; and (vi) such other measures as the Secretary determines to be appropriate. (C) Timber service business The term timber service business means a business that derives gross revenue from\u2014 (i) cutting or transporting timber from forest land; or (ii) inspecting, planting, pruning, or removing trees in a residential or commercial area. (2) Assistance for owners of nonindustrial private forest land (A) In general The Secretary shall make payments to an owner of nonindustrial private forest land that carries out an outbreak response measure to restore forest health and forest-related resources after the land is damaged by a pine beetle outbreak. (B) Cost-share requirement Payments made under subparagraph (A) shall not exceed 85 percent of the total cost of the outbreak response measures carried out by an owner of nonindustrial private forest land. (3) Assistance for timber service businesses (A) In general The Secretary shall make payments to a timber service business to cover the eligible itemized costs of the timber service business incurred in restoring forest health and forest-related resources on nonindustrial private forest land after the land is damaged by a pine beetle outbreak. (B) Cost-share requirement Payments made under subparagraph (A) shall not exceed 50 percent of the total eligible itemized costs incurred by a timber service business. (4) Eligibility and provision of payments (A) Eligibility To be eligible for a payment under paragraph (2) or (3), an owner of nonindustrial private forest land or a timber service business, respectively, shall submit to the applicable local office of the Farm Service Agency an application demonstrating that\u2014 (i) to the satisfaction of the local office, the nonindustrial private forest land on which the outbreak response measures are carried out had tree cover immediately before the pine beetle outbreak; (ii) the nonindustrial private forest land is located in a county that the Secretary has designated as a primary natural disaster area due to drought, wildfire, hurricane or excessive winds, an ice storm or blizzard, a flood, or any other resource-impacting event during the preceding 12-month period; and (iii) forest pest surveys conducted by the Forest Service or a State forestry agency confirm pine beetle infestations on or within a reasonable distance from the nonindustrial private forest land on which the outbreak response measures are carried out. (B) Implementation by local offices The local offices of the Farm Service Agency, in consultation with the applicable county committees of the Farm Service Agency, shall\u2014 (i) determine whether applicants for payments under paragraphs (2) and (3) are eligible for the payments; and (ii) provide payments to eligible applicants. (5) Emergency outbreak public assistance grants The Secretary may provide supplemental grants to State, Tribal, and local governments to aid in the response to, and the repair of damage caused by, pine beetle outbreaks. .\n#### 3. Emergency loans\n##### (a) In general\nSection 321 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961 ) is amended\u2014\n**(1)**\nby striking subsection (d);\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby inserting ( 7 U.S.C. 2266(a) ) before the period at the end; and\n**(B)**\nby striking (c) The Secretary and inserting the following:\n(d) Family farm system The Secretary ;\n**(3)**\nby redesignating subsection (b) as subsection (c);\n**(4)**\nby striking the section designation and all that follows through (a) The Secretary in subsection (a) and inserting the following:\n321. Definitions; eligibility for loans (a) Definitions In this subtitle: (1) Able to obtain sufficient credit elsewhere The term able to obtain sufficient credit elsewhere , with respect to an applicant, means that the applicant is able to obtain sufficient credit elsewhere to finance the actual needs of the applicant at a reasonable rate and terms, taking into consideration prevailing private and cooperative rates and terms in the community in or near which the applicant resides for loans for similar purposes and periods of time. (2) Aquaculture The term aquaculture means the husbandry of aquatic organisms under a controlled or selected environment. (b) Eligible persons The Secretary ; and\n**(5)**\nby adding at the end the following:\n(e) Loans to owners of nonindustrial private forest land (1) Definitions In this subsection: (A) Nonindustrial private forest land The term nonindustrial private forest land has the meaning given the term in section 407(a) of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2206(a) ). (B) Outbreak response measure The term outbreak response measure has the meaning given the term in subsection (e)(1) of section 407 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2206 ). (2) Loans Notwithstanding any other provision of this subtitle, the Secretary may make an emergency loan to an owner of nonindustrial private forest land to carry out an outbreak response measure. (3) Amount The amount of an emergency loan under this subsection shall be not less than 75 percent of the estimated total cost of the outbreak response measures to be carried out to address a pine beetle outbreak. (4) Loan repayment options In the case of an owner of nonindustrial private forest land that receives an emergency loan under this subsection and subsequently receives a cost-share payment under subsection (e)(2) of section 407 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2206 ) with respect to the same pine beetle outbreak on the same nonindustrial private forest land, the owner may, at the option of the owner, apply the amount of the cost-share payment to the remaining principal on the emergency loan under this subsection. .\n##### (b) Conforming amendments\n**(1)**\nSection 531(a) of the Federal Crop Insurance Act ( 7 U.S.C. 1531(a) ) is amended\u2014\n**(A)**\nin paragraph (16), by striking section 321(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961(a) ) and inserting section 321(b) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961(b) ) ; and\n**(B)**\nin paragraph (18), by striking section 2501(e) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(e) ) and inserting section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ) .\n**(2)**\nSection 324(d)(1) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1964(d)(1) ) is amended, in the first sentence, by striking section 321(b) of this title and inserting section 321(c) .\n**(3)**\nSection 901(a) of the Trade Act of 1974 ( 19 U.S.C. 2497(a) ) is amended\u2014\n**(A)**\nin paragraph (5), by redesignating clauses (i) through (iii) as subparagraphs (A) through (C), respectively, and indenting the subparagraphs appropriately;\n**(B)**\nin paragraph (16), by striking section 321(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961(a) ) and inserting section 321(b) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961(b) ) ; and\n**(C)**\nin paragraph (18), by striking section 2501(e) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(e) ) and inserting section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ) .\n**(4)**\nSection 582(d)(1) of the National Flood Insurance Reform Act of 1994 ( 42 U.S.C. 5154a(d)(1) ) is amended by striking section 321(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961(a) ) and inserting section 321(b) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961(b) ) .",
      "versionDate": "2025-09-18",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T16:13:39Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2872is.xml"
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
      "title": "Emergency Pine Beetle Response Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emergency Pine Beetle Response Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Credit Act of 1978 to authorize assistance for emergency measures in response to pine beetle outbreaks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:23Z"
    }
  ]
}
```
