# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/985
- Title: PROTECT USA Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 985
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-03-19T14:55:33Z
- Update date including text: 2026-03-19T14:55:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/985",
    "number": "985",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "PROTECT USA Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T14:55:33Z",
    "updateDateIncludingText": "2026-03-19T14:55:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:32:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s985is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 985\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Hagerty introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit entities integral to the national interests of the United States from participating in any foreign sustainability due diligence regulation, including the Corporate Sustainability Due Diligence Directive of the European Union, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prevent Regulatory Overreach from Turning Essential Companies into Targets Act of 2025 or the PROTECT USA Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe ability of citizens of the United States to engage in international commerce is a fundamental concern of the policy of the United States.\n**(2)**\nEntities in the extractive and manufacturing sectors contribute significantly to the prosperity of the United States and the growth of the world economy.\n**(3)**\nMaintaining and, in some cases, increasing access to certain supplies and materials from the extractive sector, including agriculture, energy, mining, and timber, and access to materials from the manufacturing sector, are critically important for promoting economic development and human progress in the United States and around the world.\n**(4)**\nRestrictions, particularly restrictions adopted unilaterally by foreign countries that are substantially different from restrictions applied by the United States, that unreasonably hinder the ability of entities integral to the national interests of the United States to pursue their commercial activities can have serious adverse effects on employment, economic stability, scientific progress, and international trade, with the potential to impede domestic and foreign policy goals.\n#### 3. Definitions\nIn this Act:\n**(1) Entity integral to the national interests of the United States**\nThe term entity integral to the national interests of the United States means any partnership, corporation, limited liability company, or other business entity that\u2014\n**(A)**\ndoes business with any part of the Federal Government, including Federal contract awards or leases;\n**(B)**\nis organized under the laws of any State or territory within the United States, or of the District of Columbia, or under any Act of Congress or a foreign subsidiary of any such entity that\u2014\n**(i)**\nderives not less than 25 percent of its revenue from activities related to the extraction or production of raw materials from the earth, including\u2014\n**(I)**\ncultivating biomass (whether or not for human consumption);\n**(II)**\nexploring or producing fossil fuels;\n**(III)**\nmining; and\n**(IV)**\nprocessing any material derived from an activity described in subclause (I), (II), or (III) for human use or benefit;\n**(ii)**\nhas a primary North American Industry Classification System code or foreign equivalent associated with the manufacturing sector;\n**(iii)**\nderives not less than 25 percent of its revenue from activities related to the mechanical, physical, or chemical transformation of materials, substances, or components into new products; or\n**(iv)**\nis engaged in\u2014\n**(I)**\nthe production of arms or other products integral to the national defense of the United States; or\n**(II)**\nthe production, mining, or processing of any critical mineral; or\n**(C)**\nthe President otherwise identifies as integral to the national interests of the United States.\n**(2) Critical mineral**\nThe term critical mineral includes\u2014\n**(A)**\nany mineral identified as a critical mineral in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ); or\n**(B)**\nany fuel mineral, including fossil fuels and any fraction, distillate, or other by-product of a fuel mineral.\n**(3) Foreign sustainability due diligence regulation**\n**(A) In general**\nExcept as provided in subparagraph (B), the term foreign sustainability due diligence regulation means any law, regulation, or other legal instrument adopted by a foreign government that requires any person to undertake\u2014\n**(i)**\nan assessment of the environmental or social impacts of its operations or value chain;\n**(ii)**\naction to address any impacts identified in the assessment described in clause (i); and\n**(iii)**\nreporting of the impacts and actions described in clauses (i) and (ii).\n**(B) Exception**\nThe term foreign sustainability due diligence regulation does not apply to any law, regulation, or other legal instrument that is substantively similar to a law, regulation, or other legal instrument that has been adopted or approved by an Act of Congress.\n**(C) Inclusion of Corporate Sustainability Due Diligence Directive**\nThe term foreign sustainability due diligence regulation includes\u2014\n**(i)**\nthe entirety of the Corporate Sustainability Due Diligence Directive adopted by the European Union;\n**(ii)**\nany successor directive adopted by the European Union or any member country of the European Union; and\n**(iii)**\nany precursor directive adopted by any member country of the European Union.\n#### 4. Prohibition on compliance with foreign sustainability due diligence regulations\n##### (a) In general\nExcept as provided in subsection (b), no entity integral to the national interests of the United States may comply with any foreign sustainability due diligence regulation.\n##### (b) Exception for ordinary business activities\nSubsection (a) does not prohibit an entity from undertaking actions that it may lawfully take\u2014\n**(1)**\nto comply with a statute of the United States; or\n**(2)**\nin the ordinary course of business.\n##### (c) Hardship relief process\n**(1) Petition for relief**\nAny entity integral to the national interests of the United States that believes it will experience particular hardship in connection with the prohibition described in subsection (a) may petition the President for an exemption from such prohibition.\n**(2) Decision**\nNot later than 30 days after the date on which the President receives a petition from an entity submitted under paragraph (1), the President shall provide a written decision to the entity that\u2014\n**(A)**\ngrants or denies the requested exemption;\n**(B)**\ncontains a statement setting forth the basis for the decision; and\n**(C)**\nin the case of a granted exemption, describes any condition that the exemption is subject to, as determined by the President.\n**(3) Factors to be considered**\nIn making the decision required by paragraph (2), the President shall consider\u2014\n**(A)**\nthe extent to which the denial of a petition submitted under paragraph (1) by an entity would result in the inability of the entity to participate in value chains associated with products essential for domestic use in the United States;\n**(B)**\npossible adverse effects on the economy in any locality or region of the United States, including adverse effects on employment;\n**(C)**\nthe degree to which granting the petition would impact, directly or indirectly, the United States; and\n**(D)**\nthe extent to which denial of the petition would prevent the entity from divesting in a business formed under the laws of a jurisdiction subject to a foreign sustainability due diligence regulation.\n#### 5. Prohibition against adverse action for compliance with this Act\n##### (a) In general\nNo person may take any adverse action towards an entity integral to the national interests of the United States for action or inaction related to a foreign sustainability due diligence regulation.\n##### (b) Judgments for foreign sustainability due diligence regulations\nNo judgment by a foreign court brought against an entity integral to the national interests of the United States in relation to any foreign sustainability due diligence regulation shall be recognized in the courts of the United States or of the States, unless otherwise provided by an Act of Congress.\n##### (c) Enforcement\n**(1) Actions by the President**\n**(A) In general**\nThe President shall take any action the President determines is in the public interest to protect an entity integral to the national interests of the United States from an adverse action related to a foreign sustainability due diligence regulation.\n**(B) Determination of public interest**\nIn determining under subparagraph (A) whether an action by the President is in the public interest, the President shall take into account the impact of the adverse action described in that subparagraph on\u2014\n**(i)**\nconsumers and businesses in the United States;\n**(ii)**\nthe economic, energy, and environmental security of the United States; and\n**(iii)**\nforeign relations of the United States, including existing international commitments.\n**(2) Private right of action**\n**(A) In general**\nAny entity integral to the national interests of the United States aggrieved by a violation of subsection (a) may bring a civil action against the person that violated subsection (a) in an appropriate district court of the United States.\n**(B) Relief**\nIn a civil action brought under subparagraph (A) in which the plaintiff prevails, the court may award\u2014\n**(i)**\na writ of mandamus or other equitable or declaratory relief;\n**(ii)**\npunitive damages not to exceed the maximum penalty described in paragraph (3)(A);\n**(iii)**\nreasonable attorney fees and litigation costs;\n**(iv)**\ncompensatory damages, including any amount paid by the entity pursuant to the applicable foreign sustainability due diligence regulation; and\n**(v)**\nall other appropriate relief.\n**(3) Penalties**\nA person that violates subsection (a) or a regulation issued pursuant to this Act\u2014\n**(A)**\nshall be subject to a civil penalty of not more than $1,000,000; and\n**(B)**\nmay, at the discretion of the President, for a period of not longer than 3 years from the date on which the person is found in violation, be deemed ineligible to submit a bid for any Federal award or contract.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-07-02",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4279",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PROTECT USA Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-05-15T00:49:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s985",
          "measure-number": "985",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s985v00",
            "update-date": "2026-03-19"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Prevent Regulatory Overreach from Turning Essential Companies into Targets Act of 2025 or the PROTECT USA Act of 2025</strong><br/>\u00a0<br/>This bill prohibits businesses integral to U.S. national interests from complying with certain foreign sustainability regulations, including the European Union's Corporate Sustainability Due Diligence Directive.<br/>\u00a0<br/>Specifically, any business entity integral to U.S. national interests is barred from complying with any foreign sustainability due diligence regulation (i.e., any foreign law, regulation, or legal instrument that requires a person to assess the environmental or social impacts of its operations or value chain, take actions to address those impacts, and report on those impacts and actions).<br/>\u00a0<br/>Entities covered by this bill include those that do business with any part of the federal government, including by way of federal contracts or leases. Other covered entities include those businesses organized under the laws of the United States that (1) derive at least 25% of their revenue from activities related to the extraction or production of raw materials from the earth, (2) are primarily involved in manufacturing, or (3) produce arms or other products\u00a0integral to U.S. national defense.<br/>\u00a0<br/>The bill prohibits adverse action against entities that comply with this prohibition and requires the President to take action in the public interest to protect such entities from an adverse action. Affected entities may bring a civil action against persons who have taken an adverse action.\u00a0Penalties for violators include up to a $1 million fine and three years of ineligibility for federal awards or contracts.</p>"
        },
        "title": "PROTECT USA Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s985.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prevent Regulatory Overreach from Turning Essential Companies into Targets Act of 2025 or the PROTECT USA Act of 2025</strong><br/>\u00a0<br/>This bill prohibits businesses integral to U.S. national interests from complying with certain foreign sustainability regulations, including the European Union's Corporate Sustainability Due Diligence Directive.<br/>\u00a0<br/>Specifically, any business entity integral to U.S. national interests is barred from complying with any foreign sustainability due diligence regulation (i.e., any foreign law, regulation, or legal instrument that requires a person to assess the environmental or social impacts of its operations or value chain, take actions to address those impacts, and report on those impacts and actions).<br/>\u00a0<br/>Entities covered by this bill include those that do business with any part of the federal government, including by way of federal contracts or leases. Other covered entities include those businesses organized under the laws of the United States that (1) derive at least 25% of their revenue from activities related to the extraction or production of raw materials from the earth, (2) are primarily involved in manufacturing, or (3) produce arms or other products\u00a0integral to U.S. national defense.<br/>\u00a0<br/>The bill prohibits adverse action against entities that comply with this prohibition and requires the President to take action in the public interest to protect such entities from an adverse action. Affected entities may bring a civil action against persons who have taken an adverse action.\u00a0Penalties for violators include up to a $1 million fine and three years of ineligibility for federal awards or contracts.</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119s985"
    },
    "title": "PROTECT USA Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prevent Regulatory Overreach from Turning Essential Companies into Targets Act of 2025 or the PROTECT USA Act of 2025</strong><br/>\u00a0<br/>This bill prohibits businesses integral to U.S. national interests from complying with certain foreign sustainability regulations, including the European Union's Corporate Sustainability Due Diligence Directive.<br/>\u00a0<br/>Specifically, any business entity integral to U.S. national interests is barred from complying with any foreign sustainability due diligence regulation (i.e., any foreign law, regulation, or legal instrument that requires a person to assess the environmental or social impacts of its operations or value chain, take actions to address those impacts, and report on those impacts and actions).<br/>\u00a0<br/>Entities covered by this bill include those that do business with any part of the federal government, including by way of federal contracts or leases. Other covered entities include those businesses organized under the laws of the United States that (1) derive at least 25% of their revenue from activities related to the extraction or production of raw materials from the earth, (2) are primarily involved in manufacturing, or (3) produce arms or other products\u00a0integral to U.S. national defense.<br/>\u00a0<br/>The bill prohibits adverse action against entities that comply with this prohibition and requires the President to take action in the public interest to protect such entities from an adverse action. Affected entities may bring a civil action against persons who have taken an adverse action.\u00a0Penalties for violators include up to a $1 million fine and three years of ineligibility for federal awards or contracts.</p>",
      "updateDate": "2026-03-19",
      "versionCode": "id119s985"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s985is.xml"
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
      "title": "PROTECT USA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT USA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prevent Regulatory Overreach from Turning Essential Companies into Targets Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit entities integral to the national interests of the United States from participating in any foreign sustainability due diligence regulation, including the Corporate Sustainability Due Diligence Directive of the European Union, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:35Z"
    }
  ]
}
```
