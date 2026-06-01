# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4509?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4509
- Title: PBM Act
- Congress: 119
- Bill type: S
- Bill number: 4509
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-29T17:10:13Z
- Update date including text: 2026-05-29T17:10:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4509",
    "number": "4509",
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
    "title": "PBM Act",
    "type": "S",
    "updateDate": "2026-05-29T17:10:13Z",
    "updateDateIncludingText": "2026-05-29T17:10:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T17:08:32Z",
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
      "sponsorshipDate": "2026-05-13",
      "state": "MO"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4509is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4509\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Ms. Warren (for herself, Mr. Hawley , Mr. Fetterman , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit pharmacy benefit managers and pharmacies from being under common ownership, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Patients Before Monopolies Act or the PBM Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nPharmacy benefit managers are corporate entities that play a dominant role in pharmaceutical supply chains, determining which drugs health plans will cover for enrollees, what prices patients and health plans will pay for those drugs, and how much health plans will reimburse pharmacies for dispensing them.\n**(2)**\nThe market for pharmacy benefit manager services has become highly concentrated. As of 2025, the 6 largest pharmacy benefit managers are each integrated into large health care conglomerates that include downstream businesses such as retail, mail order, and specialty pharmacies. These conglomerates also processed more than 90 percent of the prescriptions in the United States in 2023.\n**(3)**\nThe 3 largest pharmacy benefit managers are also vertically integrated into health care platforms that include both upstream business lines, like health insurance, and downstream suppliers, like pharmacies and providers.\n**(4)**\nThe Federal Trade Commission has found that vertically integrated pharmacy benefit managers have both the ability and incentive to steer business to their own affiliated pharmacies, which reduces competition and increases prescription drug costs for patients.\n**(5)**\nPharmacy benefit managers increasingly leverage their market power to pressure smaller, unaffiliated, independent pharmacies to enter into unfavorable contracts with the largest pharmacy benefit managers. This dynamic has likely contributed to the closure of more than 7,000 pharmacies between 2019 and 2024.\n**(6)**\nSelf-preferencing of affiliated pharmacies may also allow large, vertically integrated health conglomerates to evade statutory limits on profits known as the Medical Loss Ratio. Gaming of the profit constraint using transfer pricing techniques may allow affiliated health insurance businesses to hide profits in the unregulated pharmacy business segment, costing enrollees and taxpayers money.\n**(7)**\nPursuant to its powers under article I, section 8, of the United States Constitution, Congress has the ability to create any law necessary and appropriate to regulate interstate commerce. As pharmacy benefit managers are part of large, national health conglomerates that operate across state lines, and engage in intrastate activities that also substantially relate to interstate commerce, Congress intends to regulate pharmacy benefit managers in the public interest.\n**(8)**\nIn order to eliminate the conflicts of interest described in paragraphs (1) through (7) and restore competition to the marketplace, the Federal Government should\u2014\n**(A)**\nprotect patients, independent pharmacies, and taxpayers by structurally separating vertically integrated health conglomerates;\n**(B)**\nrequire parent companies that own a pharmacy benefit manager or insurer to divest their pharmacy businesses;\n**(C)**\nenable Federal agencies, state attorneys general, and private citizens to bring civil actions to enforce the structural separation of these companies; and\n**(D)**\ngrant the Federal Trade Commission and Department of Justice additional authority to review and block future transactions that would re-create these conflicts of interest.\n#### 3. Prohibitions relating to anticompetitive pharmacy ownership and contracts\n##### (a) Prohibition on pharmacy ownership by entities providing insurance or pharmacy benefit management services\n**(1) In general**\nIt shall be unlawful for any person to both\u2014\n**(A)**\ndirectly or indirectly own, operate, control, or direct the operation of the whole or any part of a pharmacy; and\n**(B)**\ndirectly or indirectly own, operate, or control the whole or any part of\u2014\n**(i)**\nan insurance company; or\n**(ii)**\na pharmacy benefit manager.\n**(2) Divestment**\nNot later than 1 year after the date of enactment of this Act, any person in violation of paragraph (1) shall divest the pharmacy of such person.\n##### (b) Antitrust enforcement\n**(1) In general**\nBoth the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division shall have jurisdiction, jointly or separately, to enforce this section.\n**(2) Penalties for failure to divest**\n**(A) Guidance**\nNot later than 30 days after the date of enactment of this Act, the Chair of the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division shall issue guidance specifying milestones for divestment within the deadline under subsection (a)(2).\n**(B) Penalties**\n**(i) In general**\nFor any person that does not comply with the milestones specified under subparagraph (A), the Chair of the Federal Trade Commission or the Assistant Attorney General in charge of the Antitrust Division shall cause 10 percent of the profits of the person to be transferred into escrow on a monthly basis, to be\u2014\n**(I)**\nreturned to the person if divestment occurs by the deadline under subsection (a)(2); or\n**(II)**\ndeposited into the fund described in subsection (c)(7) if divestment does not occur by the deadline under subsection (a)(2).\n**(C) Trustee**\nIf divestiture does not occur by the deadline under subsection (a)(2), a divestiture trustee shall oversee the divestiture required under that paragraph. The divestiture trustee shall have the authority to sell the pharmacy.\n##### (c) Civil actions\n**(1) In general**\nWhen the Inspector General of the Department of Health and Human Services, the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice, the Federal Trade Commission, or an attorney general of a State has reason to believe that a person is in violation of subsection (a), such Inspector General, Assistant Attorney General, Federal Trade Commission or attorney general of a State may bring a civil action in an appropriate district court of the United States.\n**(2) Private right of action**\n**(A) In general**\nAn individual alleging damages as a result of a violation of this Act may bring a civil action in any court of competent jurisdiction, State or Federal.\n**(B) Relief**\nIn a civil action brought under subparagraph (A) in which the plaintiff prevails, the court may award\u2014\n**(i)**\ntreble damages;\n**(ii)**\nreasonable attorney\u2019s fees and litigation costs; and\n**(iii)**\nany other relief, including equitable or declaratory relief, that the court determines appropriate.\n**(3) Actions by State attorneys general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates subsection (a), the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief, including monetary damages.\n**(4) Injunctive and equitable relief**\nIn any action described in paragraph (1), (2), or (3), the applicable court, on a finding that a person is in violation of subsection (a), shall issue an order requiring such person\u2014\n**(A)**\nto cease and desist from such violation, and, if applicable, divest the pharmacy services of such person; and\n**(B)**\nto disgorge any revenue received from the pharmacy from the sale of prescription drugs during the period of such violation.\n**(5) Other relief**\nIn addition to any relief obtained under paragraph (1), (2), or (3), the court may grant any other equitable relief necessary to redress and prevent recurrence of the violation.\n**(6) Right to jury trial**\nEither party, upon request, shall have the right to a jury trial.\n**(7) Deposit**\nAny revenue received from the sale of prescription drugs disgorged pursuant to an action under paragraph (1) shall be deposited in a fund created by the Federal Trade Commission and distributed by the Federal Trade Commission to be put to use in the interest of serving the health care needs of the harmed community, including consumers overcharged at vertically integrated pharmacies.\n##### (d) FTC and DOJ review\n**(1) Reporting required**\nAny divestment of a pharmacy or pharmacy benefit manager required under subsection (a) shall be reported to the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice under section 7A of the Clayton Act ( 15 U.S.C. 18a ) without respect to the thresholds under subsection (a)(2) of that section.\n**(2) Tolling of divestment period during review**\nThe divestment period under subsection (a) shall be tolled during the pendency of any waiting period required under section 7A of the Clayton Act ( 15 U.S.C. 18a ).\n**(3) Review of effect of divestiture**\nWith respect to each divestiture undertaken pursuant to subsection (a), in addition to any applicable review under section 7A of the Clayton Act ( 15 U.S.C. 18a ), the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice shall review the effect on competition, financial viability, and the public interest\u2014\n**(A)**\nof the divestiture; and\n**(B)**\nof the subsequent acquisition of the divested pharmacy by the acquiring person.\n**(4) Blocking of actions**\nThe Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice, jointly or separately, may bring a civil action in any court of competent jurisdiction to block any action that would harm competition to the detriment of the public interest with respect to the conflicts of interest described in subsection (a).\n##### (e) Rulemaking authority\nThe Federal Trade Commission shall promulgate rules to carry out this section. Such rules shall not diminish any obligation under this section.\n##### (f) Reports required\nThe Chair of the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice shall submit to the appropriate congressional committees quarterly reports on compliance with this Act, including the status of any divestitures required under this Act.\n##### (g) Rule of construction\nNothing in this section shall be construed to limit the authority of the Federal Trade Commission, the Inspector General of the Department of Justice, the Department of Health and Human Services, or the attorney general of a State under any other provision of law.\n##### (h) Severability\nIf any provision of this Act or the application thereof to any person or circumstance is held invalid, the remainder of this Act, or the application of that provision to persons or circumstances other than those as to which it is held invalid, shall not be affected thereby.\n##### (i) Definitions\nIn this section:\n**(1) Health plan**\nThe term health plan means any public or private health insurance plan.\n**(2) Person**\nThe term person has the meaning given the term in section 8 of the Sherman Act ( 15 U.S.C. 7 ).\n**(3) Pharmacy**\n**(A) In general**\nThe term pharmacy means any person, business, or entity licensed, registered, or otherwise permitted by a State or a territory of the United States to dispense, deliver, or distribute a controlled substance, prescription drug, or other medication\u2014\n**(i)**\nto the general public; or\n**(ii)**\nto a bed patient for immediate administration.\n**(B) Inclusions**\nThe term pharmacy includes\u2014\n**(i)**\na mail-order pharmacy;\n**(ii)**\na specialty pharmacy;\n**(iii)**\na retail pharmacy;\n**(iv)**\na nursing home pharmacy;\n**(v)**\na long-term care pharmacy;\n**(vi)**\na hospital pharmacy;\n**(vii)**\nan infusion or other outpatient treatment pharmacy;\n**(viii)**\nany organization the National Provider Identifier (NPI) registration of which has 1 or more taxonomy codes under the pharmacy section of the National Uniform Claim Committee (or a subsequent organization); and\n**(ix)**\nany other type of pharmacy.\n**(4) Pharmacy benefit manager**\nThe term pharmacy benefit manager means any person, business, or other entity, such as a third-party administrator, regardless of whether such person, business, or entity identifies itself as a pharmacy benefit manager, that, either directly or indirectly through an intermediary (including an affiliate, subsidiary, or agent) or an arrangement with a third party\u2014\n**(A)**\nacts as a negotiator of prices, rebates, fees, or discounts for prescription drugs on behalf of a health plan or health plan sponsor;\n**(B)**\ncontracts with pharmacies to create pharmacy networks and designs and manages such networks; or\n**(C)**\nmanages or administers the prescription drug benefits provided by a health plan, including the processing and payment of claims for prescription drugs, arranging alternative access to or funding for prescription drugs, the performance of utilization management services, including drug utilization review, the processing of drug prior authorization requests, the adjudication of appeals or grievances related to the prescription drug benefit, contracting with network pharmacies, controlling the cost of covered prescription drugs, or the provision of related services.",
      "versionDate": "2026-05-13",
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
        "updateDate": "2026-05-29T17:10:13Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4509is.xml"
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
      "title": "PBM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PBM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Patients Before Monopolies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit pharmacy benefit managers and pharmacies from being under common ownership, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:36Z"
    }
  ]
}
```
