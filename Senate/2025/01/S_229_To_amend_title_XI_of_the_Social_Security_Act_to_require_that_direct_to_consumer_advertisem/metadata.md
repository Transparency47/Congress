# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/229
- Title: DTC Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 229
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-12-05T22:02:48Z
- Update date including text: 2025-12-05T22:02:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S337-338; Sponsor introductory remarks on measure: CR S337)
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S337-338; Sponsor introductory remarks on measure: CR S337)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/229",
    "number": "229",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "DTC Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:02:48Z",
    "updateDateIncludingText": "2025-12-05T22:02:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S337-338; Sponsor introductory remarks on measure: CR S337)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T20:36:47Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-23",
      "state": "ME"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "WI"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s229is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 229\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Durbin (for himself, Mr. Grassley , Mr. King , Ms. Ernst , Ms. Smith , Mr. Welch , Mr. Blumenthal , Ms. Baldwin , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to require that direct-to-consumer advertisements for prescription drugs and biological products include an appropriate disclosure of pricing information.\n#### 1. Short title\nThis Act may be cited as the Drug-price Transparency for Consumers Act of 2025 or the DTC Act of 2025 .\n#### 2. Findings; sense of the Senate\n##### (a) Findings\nCongress finds the following:\n**(1)**\nDirect-to-consumer advertising of prescription pharmaceuticals is legally permitted in only 2 developed countries, the United States and New Zealand.\n**(2)**\nIn 2018, pharmaceutical ad spending exceeded $6,046,000,000, a 4.8-percent increase over 2017, resulting in the average American seeing 9 drug advertisements per day.\n**(3)**\nThe most commonly advertised medication in the United States in 2020 had a list price of more than $6,000 for a one-month supply.\n**(4)**\nA 2021 Government Accountability Office report found that two-thirds of all direct-to-consumer drug advertising between 2016 and 2018 was concentrated among 39 brand-name drugs or biologicals, about half of which were recently approved by the Food and Drug Administration.\n**(5)**\nAccording to a 2011 Congressional Budget Office report, pharmaceutical manufacturers advertise their products directly to consumers in an attempt to boost demand for their products and thereby raise the price that consumers are willing to pay, increase the quantity of drugs sold, or achieve some combination of the two.\n**(6)**\nStudies, including a 2012 systematic review published in the Annual Review of Public Health, a 2005 randomized trial published in the Journal of the American Medical Association, and a 2004 survey published in Health Affairs, show that patients are more likely to ask their doctor for a specific medication, and the doctor is more likely to write a prescription for it, if a patient has seen an advertisement for such medication, even if such medication is not the most clinically appropriate for the patient or if a lower cost generic medication may be available.\n**(7)**\nAccording to a 2011 Congressional Budget Office report, the average number of prescriptions written for newly approved brand-name drugs with direct-to-consumer advertising was 9 times greater than the average number of prescriptions written for newly approved brand-name drugs without direct-to-consumer advertising.\n**(8)**\nThe Centers for Medicare & Medicaid Services is the single largest drug payer in the United States. Between 2016 and 2018, 58 percent of the $560,000,000,000 in Medicare drug spending was for advertised drugs, and in 2018 alone, the 20 most advertised drugs on television cost Medicare and Medicaid a combined $34,000,000,000.\n**(9)**\nA 2021 Government Accountability Office report found that direct-to-consumer advertising may have contributed to increases in Medicare beneficiary use and spending among certain drugs.\n**(10)**\nThe American Medical Association has passed resolutions supporting the requirement for price transparency in any direct-to-consumer advertising, stating that such advertisements on their own inflate demand for new and more expensive drugs, even when these drugs may not be appropriate .\n**(11)**\nA 2019 study published in the Journal of the American Medical Association found that health care consumers dramatically underestimate their out-of-pocket costs for certain expensive medications, but once they learn the wholesale acquisition cost (in this section referred to as the WAC ) of the product, they are far better able to approximate their out-of-pocket costs.\n**(12)**\nApproximately half of Americans have high-deductible health plans, under which they often pay the list price of a drug until their insurance deductible is met. All of the top Medicare prescription drug plans use coinsurance rather than fixed-dollar copayments for medications on nonpreferred drug tiers, exposing beneficiaries to WAC prices.\n**(13)**\nSection 119 of division CC of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ) requires the Secretary of Health and Human Services to increase the use of real-time benefit tools to lower beneficiary costs. However, there still remains a lack of available pricing tools, so patients may not learn of their medication\u2019s cost until after being given a prescription for the medication. A 2013 study published in The Oncologist found that one-quarter of all cancer patients chose not to fill a prescription due to cost.\n**(14)**\nThe Federal Government already exercises its authority to oversee certain aspects of direct-to-consumer drug advertising, including required disclosures of information related to side effects, contraindications, and effectiveness.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\na lack of transparency in pricing for pharmaceuticals has led to a lack of competition for such pharmaceuticals, as evidenced by a finding by the Department of Health and Human Services that Consumers of pharmaceuticals are currently missing information that consumers of other products can more readily access, namely the list price of the product, which acts as a point of comparison when judging the reasonableness of prices offered for potential substitute products (84 Fed. Reg. 20735);\n**(2)**\nin an age where price information is ubiquitous, the prices of pharmaceuticals remain shrouded in secrecy and limited to those who subscribe to expensive drug price reporting services, which typically include pharmaceutical manufacturers or other health care industry entities and not the general public;\n**(3)**\ngreater insight and transparency into drug prices will help consumers know if they can afford to complete a course of therapy before deciding to initiate that course of therapy;\n**(4)**\nprice shopping is the mark of rational economic behavior, and markets operate more efficiently when consumers have relevant information about a product, including its price, before making an informed decision about whether to buy that product;\n**(5)**\nproviding consumers with basic price information may result in the selection of lesser cost alternatives, all else being equal relative to the patient\u2019s care, and is integral to providing adequate competition in the market;\n**(6)**\nthe WAC is a factual, objective, and uncontroversial definition for the list price of a medication, in that it is defined in statute, reflects an understood place in the supply chain, and is at the sole discretion of the manufacturer to set;\n**(7)**\nthere is a governmental interest in ensuring that consumers who seek to purchase pharmaceuticals for purposes of promoting their health and safety understand the objective list price of any pharmaceutical that they are encouraged through advertisements to purchase, which allows consumers to make informed purchasing decisions; and\n**(8)**\nthere is a governmental interest in mitigating wasteful expenditures and promoting the efficient administration of the Medicare program by slowing the growth of Federal spending on prescription drugs.\n#### 3. Requirement that direct-to-consumer advertisements for prescription drugs and biological products include an appropriate disclosure of pricing information\nPart A of title XI of the Social Security Act is amended by adding at the end the following new section:\n1150D. Requirement that direct-to-consumer advertisements for prescription drugs and biologicals include an appropriate disclosure of pricing information (a) Requirement (1) In general Subject to paragraph (2), not later than July 1, 2026, the Secretary shall require that each direct-to-consumer advertisement for a prescription drug or biological product for which payment is available under title XVIII or XIX and that is required to include the information relating to side effects, contraindications, and effectiveness described in section 202.1(e)(1) of title 21, Code of Federal Regulations (or any successor regulation) also include an appropriate disclosure of pricing information, as described in subsection (b), with respect to such prescription drug or biological product. (2) Exemption The requirement under paragraph (1) shall not apply to a prescription drug or biological product for which the wholesale acquisition cost for a 30-day supply of (or, if applicable, a typical course of treatment as set forth in the approved label for the primary indication addressed in the advertisement for) such prescription drug or biological product is less than $35. (b) Appropriate disclosure of pricing information For the purposes of subsection (a), an appropriate disclosure of pricing information, with respect to a prescription drug or biological product\u2014 (1) shall clearly and conspicuously disclose the wholesale acquisition cost for a 30-day supply of (or, if applicable, a typical course of treatment for) such prescription drug or biological product; and (2) may explain that a consumer may pay a different amount for such prescription drug or biological product than such wholesale acquisition cost depending on the health insurance coverage of the consumer. (c) Rulemaking Not later than 1 year after the date of enactment of this section, the Secretary shall promulgate final regulations to carry out this section, including establishing requirements for\u2014 (1) the visual and audio components, with respect to each medium of direct-to-consumer advertisement, to communicate the wholesale acquisition cost of the advertised prescription drug or biological product; and (2) the amount of time for a manufacturer to update any direct-to-consumer advertisement to reflect any change to the wholesale acquisition cost of the advertised prescription drug or biological product. (d) Sanctions Any manufacturer of a prescription drug or biological product, or an agent of such manufacturer, that violates the requirement of this section may be subject to a civil money penalty of not more than $100,000 for each such violation. The provisions of section 1128A (other than subsections (a) and (b)) shall apply to civil money penalties under the preceding sentence in the same manner as they apply to a penalty or proceeding under section 1128A(a). (e) Public reporting In order to enforce the requirement under this section, the Secretary may use information reported about manufacturers that fail to comply with such requirement. (f) Definitions In this section: (1) Biological product The term biological product means any biological product (as defined in section 351(i) of the Public Health Service Act) that is licensed by the Food and Drug Administration pursuant to section 351 and is subject to the requirements of section 503(b)(1) of the Federal Food, Drug, and Cosmetic Act. (2) Prescription drug The term prescription drug means any drug (as defined in section 201(g) of the Federal Food, Drug, and Cosmetic Act) that has been approved by the Food and Drug Administration pursuant to section 505 of such Act and is subject to the requirements of section 503(b)(1) of such Act. (3) Wholesale acquisition cost The term wholesale acquisition cost has the meaning given such term in section 1847A(c)(6)(B). (g) Authorization of appropriations There are authorized to be appropriated such sums as may be necessary for the purposes of carrying out this section. .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-06-05",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3789",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DTC Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-21T19:52:06Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-21T19:52:12Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-03-21T19:52:00Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-21T19:51:41Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-03-21T19:51:54Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-03-21T19:51:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T21:00:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s229",
          "measure-number": "229",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s229v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Drug-price Transparency for Consumers Act of 2025 or the DTC Act of 2025</strong><br/><br/>This bill requires consumer advertisements for\u00a0prescription drugs and biological products to include certain price information if the drug or biologic is (1) covered under Medicare or Medicaid, and (2) required to include a risk summary under current law.</p><p>Specifically, such advertisements must clearly and conspicuously disclose the wholesale price for a 30-day supply of the drug or biologic and may explain that a consumer may pay a different amount for the drug or biologic depending on the consumer's health insurance coverage.</p><p>The requirement does not apply to advertisements for drugs or\u00a0biologics with a wholesale cost of less than $35 for a one-month supply.<br/><br/>Each violation of this requirement is subject to a civil penalty of not more than $100,000.</p>"
        },
        "title": "DTC Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s229.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Drug-price Transparency for Consumers Act of 2025 or the DTC Act of 2025</strong><br/><br/>This bill requires consumer advertisements for\u00a0prescription drugs and biological products to include certain price information if the drug or biologic is (1) covered under Medicare or Medicaid, and (2) required to include a risk summary under current law.</p><p>Specifically, such advertisements must clearly and conspicuously disclose the wholesale price for a 30-day supply of the drug or biologic and may explain that a consumer may pay a different amount for the drug or biologic depending on the consumer's health insurance coverage.</p><p>The requirement does not apply to advertisements for drugs or\u00a0biologics with a wholesale cost of less than $35 for a one-month supply.<br/><br/>Each violation of this requirement is subject to a civil penalty of not more than $100,000.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119s229"
    },
    "title": "DTC Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Drug-price Transparency for Consumers Act of 2025 or the DTC Act of 2025</strong><br/><br/>This bill requires consumer advertisements for\u00a0prescription drugs and biological products to include certain price information if the drug or biologic is (1) covered under Medicare or Medicaid, and (2) required to include a risk summary under current law.</p><p>Specifically, such advertisements must clearly and conspicuously disclose the wholesale price for a 30-day supply of the drug or biologic and may explain that a consumer may pay a different amount for the drug or biologic depending on the consumer's health insurance coverage.</p><p>The requirement does not apply to advertisements for drugs or\u00a0biologics with a wholesale cost of less than $35 for a one-month supply.<br/><br/>Each violation of this requirement is subject to a civil penalty of not more than $100,000.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119s229"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s229is.xml"
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
      "title": "DTC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:47Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DTC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Drug-price Transparency for Consumers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to require that direct-to-consumer advertisements for prescription drugs and biological products include an appropriate disclosure of pricing information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:29Z"
    }
  ]
}
```
