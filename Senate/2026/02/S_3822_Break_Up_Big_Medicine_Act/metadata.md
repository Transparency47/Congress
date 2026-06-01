# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3822
- Title: Break Up Big Medicine Act
- Congress: 119
- Bill type: S
- Bill number: 3822
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-02-27T19:08:48Z
- Update date including text: 2026-02-27T19:08:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3822",
    "number": "3822",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Break Up Big Medicine Act",
    "type": "S",
    "updateDate": "2026-02-27T19:08:48Z",
    "updateDateIncludingText": "2026-02-27T19:08:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T20:56:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2026-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3822is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3822\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Ms. Warren (for herself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit pharmacy benefit managers, insurers, and prescription drug or medical device wholesalers from being under common ownership with certain medical service providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Break Up Big Medicine Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nLarge, vertically integrated health care platforms dominate the American health care system. These corporate entities own or control every part of the health care supply chain, including upstream business lines, like health insurance plans, and downstream suppliers, like pharmacies and physicians. This is the end result of an unprecedented wave of consolidation.\n**(2)**\nLarge, publicly traded insurance conglomerates have increasingly engaged in aggressive acquisition strategies, becoming some of the largest employers of physicians in the country. As of 2023, one conglomerate controls approximately 10 percent of all American physicians, making it the single largest employer of physicians in the nation.\n**(3)**\nMore than three-quarters of all American doctors are employed by corporate entities, with independent physicians comprising a small and shrinking share of America\u2019s doctors.\n**(4)**\nLarge wholesalers of drugs and medical devices have similarly engaged in a wave of consolidation. The 3 largest drug wholesalers control 98 percent of the United States drug distribution market. These conglomerates have also engaged in substantial vertical integration, acquiring downstream suppliers including specialty medical practices and medical supply distributors. Since January 2024, the 3 largest drug wholesalers have proposed or completed acquisitions of downstream suppliers worth approximately $16,000,000,000 and spanning more than 1,000 locations across 35 States.\n**(5)**\nPharmacy benefit managers are corporate entities that determine what drugs will be covered by health plans, what prices patients will pay, and how much pharmacies will be reimbursed. The 3 largest pharmacy benefit managers are each integrated into large, corporate health care platforms. These 3 pharmacy benefit managers alone process nearly 80 percent of prescription drug claims.\n**(6)**\nOwnership of both upstream and downstream businesses creates inherent conflicts of interest for corporate health care platforms.\n**(A)**\nThe Federal Trade Commission has found that vertically integrated pharmacy benefit managers have both the ability and incentive to steer business to their own affiliated pharmacies, which reduces competition and increases prescription drug costs for patients.\n**(B)**\nIn the physician market, large insurers have the ability and incentive to steer enrollees to providers owned by the same parent company.\n**(C)**\nSelf-preferencing of affiliated pharmacies or physicians may allow large, vertically integrated health conglomerates to evade statutory limits on profits known as the Medical Loss Ratio. Gaming of the profit constraint using transfer pricing techniques may allow affiliated health insurance businesses to hide profits in the unregulated pharmacy or physician business segments, costing enrollees and taxpayers money.\n**(D)**\nExtensive evidence supports claims that private insurers issuing Medicare Advantage plans use employed physicians to intensively document the medical conditions of their enrollees, generating inflated payments from the Federal Government without improving care quality.\n**(E)**\nIn the wholesale drug distribution market, acquisitions of specialty care providers by large wholesalers can create the incentive and ability for the new, vertically integrated company to steer specialists toward prescribing the most lucrative drugs and devices rather than the best treatment for the patient.\n**(7)**\nPursuant to its powers under article I, section 8, of the United States Constitution, Congress has the ability to create any law necessary and appropriate to regulate interstate commerce. Large, national health conglomerates operate across state lines and engage in intrastate activities that substantially relate to interstate commerce. Congress intends to regulate these corporate health care platforms in the public interest.\n**(8)**\nIn order to eliminate the conflicts of interest described in paragraphs (1) through (7) and restore competition to the marketplace, the Federal Government should\u2014\n**(A)**\nprotect patients, physicians, pharmacies, and taxpayers by structurally separating vertically integrated health conglomerates;\n**(B)**\nrequire parent companies that own an insurer or pharmacy benefit manager to divest any medical providers they either directly own or control through management service organizations;\n**(C)**\nrequire parent companies that own a prescription drug or medical device wholesaler to divest any medical provider or management service organizations they own;\n**(D)**\nenable Federal agencies, State attorneys general, and private citizens to bring civil actions to enforce the structural separation of these companies; and\n**(E)**\ngrant the Federal Trade Commission and Department of Justice additional authority to review and block future actions that would harm the public interest by re-creating the conflicts of interest described above.\n#### 3. Prohibitions relating to anticompetitive ownership and contracts\n##### (a) Prohibition on certain common ownership\n**(1) Involving an insurance company or pharmacy benefit manager**\n**(A) In general**\nIt shall be unlawful for any person to both\u2014\n**(i)**\ndirectly or indirectly own, operate, control, or direct the operation of the whole or any part of\u2014\n**(I)**\na provider; or\n**(II)**\na management services organization; and\n**(ii)**\ndirectly or indirectly own, operate, or control the whole or any part of\u2014\n**(I)**\nan insurance company; and\n**(II)**\na pharmacy benefit manager.\n**(B) Divestment**\nNot later than 1 year after the date of enactment of this Act, any person in violation of subparagraph (A) shall divest one of the following:\n**(i)**\nAll entities described in subparagraph (A)(i).\n**(ii)**\nAll entities described in subparagraph (A)(ii).\n**(2) Involving a wholesaler**\n**(A) In general**\nIt shall be unlawful for any person to both\u2014\n**(i)**\ndirectly or indirectly own, operate, control, or direct the operation of the whole or any part of a provider or management services organization; and\n**(ii)**\ndirectly or indirectly own, operate, or control the whole or any part of a prescription drug or medical device wholesaler.\n**(B) Divestment**\nNot later than 1 year after the date of enactment of this Act, any person in violation of subparagraph (A) shall divest one of the following:\n**(i)**\nAll entities described in subparagraph (A)(i).\n**(ii)**\nAll entities described in subparagraph (A)(ii).\n##### (b) Antitrust enforcement\n**(1) In general**\nBoth the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division shall have jurisdiction, jointly or separately, to enforce this section.\n**(2) Penalties for failure to divest**\n**(A) Guidance**\nNot later than 30 days after the date of enactment of this Act, the Chair of the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division shall issue guidance specifying milestones for divestment within the deadline under subsection (a).\n**(B) Penalties**\n**(i) In general**\nFor any person that does not comply with the milestones specified under subparagraph (A), the Chair of the Federal Trade Commission or the Assistant Attorney General in charge of the Antitrust Division shall cause 10 percent of the profits of the person to be transferred into escrow on a monthly basis, to be\u2014\n**(I)**\nreturned to the person if divestment occurs by the deadline under subsection (a); or\n**(II)**\ndeposited into the fund described in subsection (c)(7) if divestment does not occur by the deadline under subsection (a).\n**(C) Trustee**\nIf divestiture does not occur by the deadline under subsection (a), a divestiture trustee shall oversee the divestiture required under that paragraph. The divestiture trustee shall have the authority to sell the entity to which the divestiture requirement applies.\n##### (c) Civil actions\n**(1) In general**\nWhen the Inspector General of the Department of Health and Human Services, the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice, the Federal Trade Commission, or an attorney general of a State has reason to believe that a person is in violation of subsection (a), such Inspector General, Assistant Attorney General, Federal Trade Commission or attorney general of a State may bring a civil action in an appropriate district court of the United States.\n**(2) Private right of action**\n**(A) In general**\nAn individual alleging damages as a result of a violation of this Act may bring a civil action in any court of competent jurisdiction, State or Federal.\n**(B) Relief**\nIn a civil action brought under subparagraph (A) in which the plaintiff prevails, the court may award\u2014\n**(i)**\ntreble damages;\n**(ii)**\nreasonable attorney\u2019s fees and litigation costs; and\n**(iii)**\nany other relief, including equitable or declaratory relief, that the court determines appropriate.\n**(3) Actions by state attorneys general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates subsection (a), the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief, including monetary damages.\n**(4) Injunctive and equitable relief**\nIn any action described in paragraph (1), (2), or (3), the applicable court, on a finding that a person is in violation of subsection (a), shall issue an order requiring such person\u2014\n**(A)**\nto cease and desist from such violation, and, if applicable, divest an entity of such person in accordance with paragraph (1)(B) or paragraph (2)(B) of such subsection (a), as applicable; and\n**(B)**\nto disgorge any revenue received from an entity subject to divestment in accordance with such subsection (a) for the period of such violation.\n**(5) Other relief**\nIn addition to any relief obtained under paragraph (1), (2), (3), or (4), the court may grant any other equitable relief necessary to redress and prevent recurrence of the violation.\n**(6) Right to jury trial**\nEither party, upon request, shall have the right to a jury trial.\n**(7) Deposit**\nAny revenue disgorged pursuant to an action under paragraph (1) shall be deposited in a fund created by the Federal Trade Commission and distributed by the Federal Trade Commission to be put to use in the interest of serving the health care needs of the harmed community, including consumers overcharged for medical services at vertically integrated health care conglomerates.\n##### (d) FTC and DOJ review\n**(1) Reporting required**\nAny divestment of an entity required under subsection (a) shall be reported to the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice under section 7A of the Clayton Act ( 15 U.S.C. 18a ) without respect to the thresholds under subsection (a)(2) of that section.\n**(2) Tolling of divestment period during review**\nThe divestment period under subsection (a) shall be tolled during the pendency of any waiting period required under section 7A of the Clayton Act ( 15 U.S.C. 18a ).\n**(3) Review of effect of divestiture**\nWith respect to each divestiture undertaken pursuant to subsection (a), in addition to any applicable review under section 7A of the Clayton Act ( 15 U.S.C. 18a ), the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice shall review the effect on competition, financial viability, and the public interest\u2014\n**(A)**\nof the divestiture; and\n**(B)**\nof the subsequent acquisition of the divested entity by the acquiring person.\n**(4) Blocking of actions**\nThe Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice, jointly or separately, may bring a civil action in any court of competent jurisdiction to block any action that would harm competition to the detriment of the public interest with respect to the conflicts of interest described in subsection (a).\n##### (e) Rulemaking authority\nThe Federal Trade Commission shall promulgate rules to carry out this section. Such rules shall not diminish any obligation under this section.\n##### (f) Reports required\nThe Chair of the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice shall submit to the appropriate congressional committees quarterly reports on compliance with this Act, including the status of any divestitures required under this Act.\n##### (g) Rule of construction\nNothing in this section shall be construed to limit the authority of the Federal Trade Commission, the Inspector General of the Department of Justice, the Department of Health and Human Services, or the attorney general of a State under any other provision of law.\n##### (h) Severability\nIf any provision of this Act or the application thereof to any person or circumstance is held invalid, the remainder of this Act, or the application of that provision to persons or circumstances other than those as to which it is held invalid, shall not be affected thereby.\n##### (i) Definitions\nIn this section:\n**(1) Drug; device**\nThe terms drug and device have the meanings given those terms, respectively, in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(2) Health plan**\nThe term health plan means any public or private health insurance plan.\n**(3) Management services organization**\nThe term management services organization means an entity that has entered into an agreement with a provider to furnish services to such provider, including services relating to payroll, human resources, employment screening, payer contracting, billing and collection, coding, information technology services, patient scheduling, property or equipment leasing, and administrative or business services that do not constitute the practice of medicine.\n**(4) Person**\nThe term person has the meaning given the term in section 8 of the Sherman Act ( 15 U.S.C. 7 ).\n**(5) Pharmacy benefit manager**\nThe term pharmacy benefit manager means any person, business, or other entity, such as a third-party administrator, regardless of whether such person, business, or entity identifies itself as a pharmacy benefit manager, that, either directly or indirectly through an intermediary (including an affiliate, subsidiary, or agent) or an arrangement with a third party\u2014\n**(A)**\nacts as a negotiator of prices, rebates, fees, or discounts for prescription drugs on behalf of a health plan or health plan sponsor;\n**(B)**\ncontracts with pharmacies to create pharmacy networks and designs and manages such networks; or\n**(C)**\nmanages or administers the prescription drug benefits provided by a health plan, including the processing and payment of claims for prescription drugs, arranging alternative access to or funding for prescription drugs, the performance of utilization management services, including drug utilization review, the processing of drug prior authorization requests, the adjudication of appeals or grievances related to the prescription drug benefit, contracting with network pharmacies, controlling the cost of covered prescription drugs, or the provision of related services.\n**(6) Prescription drug**\nThe term prescription drug means a drug approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) that is subject to section 503(b)(1) of such Act ( 21 U.S.C. 353(b)(1) ).\n**(7) Prescription drug or medical device wholesaler**\nThe term prescription drug or medical device wholesaler \u2014\n**(A)**\nmeans a person engaged in wholesale distribution of a prescription drug or a device; and\n**(B)**\nincludes a parent (direct or indirect) of, a subsidiary (direct or indirect, and partial or complete) of, and any entity under the common control or ownership of a person described in subparagraph (A).\n**(8) Provider**\nThe term provider means a practitioner or entity the National Provider Institute registration of which has 1 or more taxonomy codes under the National Uniform Claim Committee (or subsequent organization), including any in-patient or outpatient pharmacy, physician practice, ambulatory surgery center, urgent care center, post-acute care facility, home-health provider, or hospital.\n**(9) Wholesale distribution**\nThe term wholesale distribution \u2014\n**(A)**\nmeans a person engaged in the sale, purchase, trade, delivery, handling, storage or receipt of a drug or device by a person other than the consumer or patient; and\n**(B)**\ndoes not include\u2014\n**(i)**\ndispensing of a drug or device to a consumer or patient by a person having a valid license under State law to do so;\n**(ii)**\npurchase, handling, storage, receipt, or other acquisition of a drug or device by a person having a valid license under State law to dispense or administer drugs or devices or, a hospital, pharmacy, or other health care entity, for use by such person, hospital, pharmacy, or other health care entity;\n**(iii)**\nsale, purchase, trade, delivery, handling, storage, or receipt of a drug or device by a person holding an application approved under section 505 or 515 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 , 360e) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) for such drug or device, a co-licensed partner of any person described in this clause, or an affiliate of any person described in this clause;\n**(iv)**\npossession by, receipt by, or transfer to a\u2014\n**(I)**\nthird-party logistics provider that provides or coordinates warehousing or other logistics services in interstate commerce; or\n**(II)**\nrepackager who owns or operates an establishment that repacks and relabels drugs or devices for further sale or distribution, provided that such third-party logistics provider or repackager does not take ownership of the drug or device;\n**(v)**\npossession by, receipt by, or transfer to a common carrier that transports a drug or device, provided that the common carrier does not take ownership of the drug;\n**(vi)**\nintracompany transfer of any drug or device by an entity described in clause (i), (ii), or (iii), including transfers between affiliates thereof, or warehousing by such person incidental to such intracompany transfer; or\n**(vii)**\nreturns or reverse distribution by any person described in clause (i), (ii), (iii), (iv), or (v).",
      "versionDate": "2026-02-10",
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
        "name": "Health",
        "updateDate": "2026-02-27T19:08:48Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3822is.xml"
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
      "title": "Break Up Big Medicine Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Break Up Big Medicine Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit pharmacy benefit managers, insurers, and prescription drug or medical device wholesalers from being under common ownership with certain medical service providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:25Z"
    }
  ]
}
```
