# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1040?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1040
- Title: Drug Competition Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 1040
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-01-30T17:36:07Z
- Update date including text: 2026-01-30T17:36:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 43.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 43.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1040",
    "number": "1040",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Drug Competition Enhancement Act",
    "type": "S",
    "updateDate": "2026-01-30T17:36:07Z",
    "updateDateIncludingText": "2026-01-30T17:36:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 43.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
        "item": [
          {
            "date": "2025-04-10T20:27:19Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-03T14:15:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-13T18:19:27Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CT"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "IA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1040is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1040\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Cornyn (for himself, Mr. Blumenthal , Mr. Grassley , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Federal Trade Commission Act to prohibit product hopping, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug Competition Enhancement Act .\n#### 2. Product hopping\n##### (a) In general\nThe Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) is amended by inserting after section 26 ( 15 U.S.C. 57c\u20132 ) the following:\n27. Product hopping (a) Definitions In this section: (1) Abbreviated new drug application The term abbreviated new drug application means any application under subsection (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or an application under subsection (b)(2) of such section 505 that seeks a therapeutic equivalence rating to the reference product. (2) Biosimilar biological product The term biosimilar biological product means a biological product licensed under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (3) Biosimilar biological product license application The term biosimilar biological product license application means an application submitted under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (4) Follow-on product The term follow-on product \u2014 (A) means a drug approved through an application or supplement to an application submitted under section 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ) or a biological product licensed through an application or supplement to an application submitted under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ) for a change or modification to, or reformulation of, the same manufacturer\u2019s previously approved drug or biological product that has an indication that is identical or substantively similar to an indication of the same manufacturer\u2019s previously approved drug or biological product; and (B) excludes such an application or supplement to an application for a change, modification, or reformulation of a drug or biological product that is requested by the Secretary or necessary to comply with law, including sections 505A and 505B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355a , 355c). (5) Generic drug The term generic drug means any drug approved under an application submitted under subsection (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or an application under subsection (b)(2) of such section 505 that seeks a therapeutic equivalence rating to the reference product. (6) Listed drug The term listed drug means a drug listed under section 505(j)(7) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(7) ). (7) Manufacturer The term manufacturer means the holder, licensee, or assignee of\u2014 (A) an approved application for a drug under section 505(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c) ); or (B) a biological product license under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ). (8) Reference product The term reference product has the meaning given the term in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ). (9) Ultimate parent entity The term ultimate parent entity has the meaning given the term in section 801.1 of title 16, Code of Federal Regulations, or any successor regulation. (b) Prohibition on product hopping (1) Prima facie A manufacturer of a reference product or listed drug shall be considered to have engaged in an unfair method of competition in or affecting commerce in violation of section 5(a) if complaint counsel or the Commission demonstrates in an action or proceeding initiated by the Commission under subsection (c) that, during the period beginning on the date on which the manufacturer of the reference product or listed drug first receives notice that an applicant has submitted to the Commissioner of Food and Drugs an abbreviated new drug application or biosimilar biological product license application referencing the reference product or listed drug and ending on the date that is the earlier of 180 days after the date on which the generic drug or biosimilar biological product that is the subject of the abbreviated new drug application or biosimilar biological product license application or another generic drug or biosimilar biological product referencing the listed drug or reference product is first marketed or 3 years after the date on which the follow-on product is first marketed, the manufacturer engaged in either of the following actions: (A) The manufacturer engaged in a hard switch, which shall be established by demonstrating that the manufacturer engaged in either of the following actions: (i) Upon the request of the manufacturer of the listed drug or reference product, the Commissioner of Food and Drugs withdrew the approval of the application for the listed drug or reference product or placed the listed drug or reference product on the discontinued products list and the manufacturer marketed or sold a follow-on product. (ii) The manufacturer of the listed drug or reference product\u2014 (I) (aa) withdrew, discontinued the manufacture of, or announced withdrawal of, discontinuance of the manufacture of, or intent to withdraw the application with respect to the drug or reference product in a manner that impedes competition from a generic drug or a biosimilar biological product, which may be established by objective circumstances, unless such actions were taken by the manufacturer pursuant to a request of the Commissioner of Food and Drugs; or (bb) destroyed the inventory of the listed drug or reference product in a manner that impedes competition from a generic drug or a biosimilar biological product, which may be established by objective circumstances; and (II) marketed or sold a follow-on product. (B) The manufacturer engaged in a soft switch, which shall be established by demonstrating that the manufacturer engaged in both of the following actions: (i) The manufacturer took actions with respect to the listed drug or reference product other than those described in subparagraph (A) that unfairly disadvantage the listed drug or reference product relative to the follow-on product described in clause (ii) in a manner that impedes competition from a generic drug or a biosimilar biological product, which may be established by objective circumstances. (ii) The manufacturer marketed or sold a follow-on product. (2) Exclusions Nothing in this section shall prohibit actions that consist solely of\u2014 (A) truthful, non-misleading promotional marketing; or (B) ceasing promotional marketing for the listed drug or reference product. (3) Justification (A) In general Subject to paragraph (4), the actions described in paragraph (1) by a manufacturer of a listed drug or reference product shall not be considered to be an unfair method of competition in or affecting commerce if the manufacturer demonstrates to the Commission or a district court of the United States, as applicable, in an action, suit or proceeding initiated by the Commission under subsection (c)(1) that\u2014 (i) the manufacturer would have taken the actions regardless of whether a generic drug that references the listed drug or biosimilar biological product that references the reference product had already entered the market; and (ii) (I) with respect to a hard switch under paragraph (1)(A), the manufacturer took the action for reasons relating to the safety risk to patients of the listed drug or reference product; (II) with respect to an action described in paragraph (1)(A)(ii)(I)(aa), there is a supply disruption that\u2014 (aa) is outside of the control of the manufacturer; (bb) prevents the production or distribution of the applicable listed drug or reference product; and (cc) cannot be remedied by reasonable efforts; or (III) with respect to a soft switch under paragraph (1)(B), the manufacturer had legitimate pro-competitive reasons, apart from the financial effects of reduced competition, to take the action. (B) Rule of construction Nothing in subparagraph (A) may be construed to limit the information that the Commission may otherwise obtain in any proceeding or action instituted with respect to a violation of this section. (4) Response With respect to a justification offered by a manufacturer under paragraph (3), the Commission may\u2014 (A) rebut any evidence presented by a manufacturer during that justification; or (B) establish by a preponderance of the evidence that\u2014 (i) on balance, the pro-competitive benefits from the conduct described in subparagraph (A) or (B) of paragraph (1), as applicable, do not outweigh any anticompetitive effects of the conduct, even in consideration of the justification so offered; or (ii) (I) the conduct described in paragraph (1) is not reasonably necessary to address or achieve the justifications described in clause (ii) of paragraph (3)(A); or (II) the justifications described in clause (ii) of paragraph (3)(A) could be reasonably addressed or achieved through less anticompetitive means. (c) Enforcement (1) In general If the Commission has reason to believe that any manufacturer has violated, is violating, or is about to violate this section, or a rule promulgated under this section, the Commission may take any of the following actions: (A) Institute a proceeding under section 5(b). (B) In the same manner and to the same extent as provided in section 13(b), bring suit in a district court of the United States to temporarily enjoin the action of the manufacturer. (C) Bring suit in a district court of the United States, in which the Commission may seek\u2014 (i) to permanently enjoin the action of the manufacturer; (ii) any of the remedies described in paragraph (3); and (iii) any other equitable remedy, including ancillary equitable relief. (2) Judicial review (A) In general Notwithstanding any provision of section 5, any manufacturer that is subject to a final cease and desist order issued in a proceeding to enforce this section, or a rule promulgated under this section, may, not later than 30 days after the date on which the Commission issues the order, petition for review of the order in\u2014 (i) the United States Court of Appeals for the District of Columbia Circuit; or (ii) the court of appeals of the United States for the circuit in which the ultimate parent entity of the manufacturer is incorporated. (B) Treatment of findings In a review of a final cease and desist order conducted by a court of appeals of the United States under subparagraph (A), the factual findings of the Commission shall be conclusive if those facts are supported by the evidence. (3) Equitable remedies (A) Disgorgement (i) In general In a suit brought under paragraph (1)(C), the Commission may seek, and the court may order, disgorgement of any unjust enrichment that a person obtained as a result of the violation that gives rise to the suit. (ii) Calculation Any disgorgement that is ordered with respect to a person under clause (i) shall be offset by any amount of restitution ordered under subparagraph (B). (iii) Limitations period The Commission may seek disgorgement under this subparagraph not later than 5 years after the latest date on which the person from which the disgorgement is sought receives any unjust enrichment from the effects of the violation that gives rise to the suit in which the Commission seeks the disgorgement. (B) Restitution (i) In general In a suit brought under paragraph (1)(C), the Commission may seek, and the court may order, restitution with respect to the violation that gives rise to the suit. (ii) Limitations period The Commission may seek restitution under this subparagraph not later than 5 years after the latest date on which the person from which the restitution is sought receives any unjust enrichment from the effects of the violation that gives rise to the suit in which the Commission seeks the restitution. (4) Rules of construction Nothing in this subsection may be construed as\u2014 (A) requiring the Commission to bring a suit seeking a temporary injunction under paragraph (1)(B) before bringing a suit seeking a permanent injunction under paragraph (1)(C); or (B) affecting the authority of the Federal Trade Commission under any other provision of law. .\n##### (b) Applicability\nSection 27 of the Federal Trade Commission Act, as added by subsection (a), shall apply with respect to any\u2014\n**(1)**\nconduct that occurs on or after the date of enactment of this Act; and\n**(2)**\naction or proceeding that is commenced on or after the date of enactment of this Act.\n##### (c) Antitrust laws\nExcept to the extent subsection (a) establishes an additional basis for liability under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ), nothing in this section, or the amendments made by this section, shall modify, impair, limit, or supersede the applicability of the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ), or of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that it applies to unfair methods of competition.\n##### (d) Rulemaking\nThe Federal Trade Commission may issue rules under section 553 of title 5, United States Code, to define any terms used in section 27 of the Federal Trade Commission Act, as added by subsection (a) (other than terms that are defined in subsection (a) of such section 27).",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1040rs.xml",
      "text": "II\nCalendar No. 43\n119th CONGRESS\n1st Session\nS. 1040\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Cornyn (for himself, Mr. Blumenthal , Mr. Grassley , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 10, 2025 Reported by Mr. Grassley , with an amendment Omit the part struck through and insert the part printed in italic\nA BILL\nTo amend the Federal Trade Commission Act to prohibit product hopping, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug Competition Enhancement Act .\n#### 2. Product hopping\n##### (a) In general\nThe Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) is amended by inserting after section 26 ( 15 U.S.C. 57c\u20132 ) the following:\n27. Product hopping (a) Definitions In this section: (1) Abbreviated new drug application The term abbreviated new drug application means any application under subsection (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or an application under subsection (b)(2) of such section 505 that seeks a therapeutic equivalence rating to the reference product. (2) Biosimilar biological product The term biosimilar biological product means a biological product licensed under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (3) Biosimilar biological product license application The term biosimilar biological product license application means an application submitted under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (4) Follow-on product The term follow-on product \u2014 (A) means a drug approved through an application or supplement to an application submitted under section 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ) or a biological product licensed through an application or supplement to an application submitted under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ) for a change or modification to, or reformulation of, the same manufacturer\u2019s previously approved drug or biological product that has an indication that is identical or substantively similar to an indication of the same manufacturer\u2019s previously approved drug or biological product; and (B) excludes such an application or supplement to an application for a change, modification, or reformulation of a drug or biological product that is requested by the Secretary or necessary to comply with law, including sections 505A and 505B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355a , 355c). (5) Generic drug The term generic drug means any drug approved under an application submitted under subsection (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or an application under subsection (b)(2) of such section 505 that seeks a therapeutic equivalence rating to the reference product abbreviated new drug application . (6) Listed drug The term listed drug means a drug listed under section 505(j)(7) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(7) ). (7) Manufacturer The term manufacturer means the holder, licensee, or assignee of\u2014 (A) an approved application for a drug under section 505(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c) ); or (B) a biological product license under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ). (8) Reference product The term reference product has the meaning given the term in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ). (9) Ultimate parent entity The term ultimate parent entity has the meaning given the term in section 801.1 of title 16, Code of Federal Regulations, or any successor regulation. (b) Prohibition on product hopping (1) Prima facie A manufacturer of a reference product or listed drug shall be considered to have engaged in an unfair method of competition in or affecting commerce in violation of section 5(a) if complaint counsel or the Commission demonstrates in an action or proceeding initiated by the Commission under subsection (c) that, during the period beginning on the date on which the manufacturer of the reference product or listed drug first receives notice that an applicant has submitted to the Commissioner of Food and Drugs an abbreviated new drug application or biosimilar biological product license application referencing the reference product or listed drug and ending on the date that is the earlier of 180 days after the date on which the generic drug or biosimilar biological product that is the subject of the abbreviated new drug application or biosimilar biological product license application or another generic drug or biosimilar biological product referencing the listed drug or reference product is first marketed or 3 years after the date on which the follow-on product is first marketed, the manufacturer engaged in either of the following actions: (A) The manufacturer engaged in a hard switch, which shall be established by demonstrating that the manufacturer engaged in either of the following actions: (i) Upon the request of the manufacturer of the listed drug or reference product, the Commissioner of Food and Drugs withdrew the approval of the application for the listed drug or reference product or placed the listed drug or reference product on the discontinued products list and the manufacturer marketed or sold a follow-on product. (ii) The manufacturer of the listed drug or reference product\u2014 (I) (aa) withdrew, discontinued the manufacture of, or announced withdrawal of, discontinuance of the manufacture of, or intent to withdraw the application with respect to the drug or reference product in a manner that impedes competition from a generic drug or a biosimilar biological product, which may be established by objective circumstances, unless such actions were taken by the manufacturer pursuant to a request of the Commissioner of Food and Drugs; or (bb) destroyed the inventory of the listed drug or reference product in a manner that impedes competition from a generic drug or a biosimilar biological product, which may be established by objective circumstances; and (II) marketed or sold a follow-on product. (B) The manufacturer engaged in a soft switch, which shall be established by demonstrating that the manufacturer engaged in both of the following actions: (i) The manufacturer took actions with respect to the listed drug or reference product other than those described in subparagraph (A) that unfairly disadvantage the listed drug or reference product relative to the follow-on product described in clause (ii) in a manner that impedes competition from a generic drug or a biosimilar biological product, which may be established by objective circumstances. (ii) The manufacturer marketed or sold a follow-on product. (2) Exclusions Nothing in this section shall prohibit actions that consist solely of\u2014 (A) truthful, non-misleading promotional marketing; or (B) ceasing promotional marketing for the listed drug or reference product. (3) Justification (A) In general Subject to paragraph (4), the actions described in paragraph (1) by a manufacturer of a listed drug or reference product shall not be considered to be an unfair method of competition in or affecting commerce if the manufacturer demonstrates to the Commission or a district court of the United States, as applicable, in an action, suit , or proceeding initiated by the Commission under subsection (c)(1) that\u2014 (i) the manufacturer would have taken the actions regardless of whether a generic drug that references the listed drug or biosimilar biological product that references the reference product had already entered the market; and (ii) (I) with respect to a hard switch under paragraph (1)(A), the manufacturer took the action for reasons relating to the safety risk to patients of the listed drug or reference product; (II) with respect to an action described in paragraph (1)(A)(ii)(I)(aa), there is a supply disruption that\u2014 (aa) is outside of the control of the manufacturer; (bb) prevents the production or distribution of the applicable listed drug or reference product; and (cc) cannot be remedied by reasonable efforts; or (III) with respect to a soft switch under paragraph (1)(B), the manufacturer had legitimate pro-competitive reasons, apart from the financial effects of reduced competition, to take the action. (B) Rule of construction Nothing in subparagraph (A) may be construed to limit the information that the Commission may otherwise obtain in any proceeding or action instituted with respect to a violation of this section. (4) Response With respect to a justification offered by a manufacturer under paragraph (3), the Commission may\u2014 (A) rebut any evidence presented by a manufacturer during that justification; or (B) establish by a preponderance of the evidence that\u2014 (i) on balance, the pro-competitive benefits from the conduct described in subparagraph (A) or (B) of paragraph (1), as applicable, do not outweigh any anticompetitive effects of the conduct, even in consideration of the justification so offered; or (ii) (I) the conduct described in paragraph (1) is not reasonably necessary to address or achieve the justifications described in clause (ii) of paragraph (3)(A); or (II) the justifications described in clause (ii) of paragraph (3)(A) could be reasonably addressed or achieved through less anticompetitive means. (c) Enforcement (1) In general If the Commission has reason to believe that any manufacturer has violated, is violating, or is about to violate this section, or a rule promulgated under this section, the Commission may take any of the following actions: (A) Institute a proceeding under section 5(b). (B) In the same manner and to the same extent as provided in section 13(b), bring suit in a district court of the United States to temporarily enjoin the action of the manufacturer. (C) Bring suit in a district court of the United States, in which the Commission may seek\u2014 (i) to permanently enjoin the action of the manufacturer; (ii) any of the remedies described in paragraph (3); and (iii) any other equitable remedy, including ancillary equitable relief. (2) Judicial review (A) In general Notwithstanding any provision of section 5, any manufacturer that is subject to a final cease and desist order issued in a proceeding to enforce this section, or a rule promulgated under this section, may, not later than 30 days after the date on which the Commission issues the order, petition for review of the order in\u2014 (i) the United States Court of Appeals for the District of Columbia Circuit; or (ii) the court of appeals of the United States for the circuit in which the ultimate parent entity of the manufacturer is incorporated. (B) Treatment of findings In a review of a final cease and desist order conducted by a court of appeals of the United States under subparagraph (A), the factual findings of the Commission shall be conclusive if those facts are supported by the evidence. (3) Equitable remedies (A) Disgorgement (i) In general In a suit brought under paragraph (1)(C), the Commission may seek, and the court may order, disgorgement of any unjust enrichment that a person obtained as a result of the violation that gives rise to the suit. (ii) Calculation Any disgorgement that is ordered with respect to a person under clause (i) shall be offset by any amount of restitution ordered under subparagraph (B). (iii) Limitations period The Commission may seek disgorgement under this subparagraph not later than 5 years after the latest date on which the person from which the disgorgement is sought receives any unjust enrichment from the effects of the violation that gives rise to the suit in which the Commission seeks the disgorgement. (B) Restitution (i) In general In a suit brought under paragraph (1)(C), the Commission may seek, and the court may order, restitution with respect to the violation that gives rise to the suit. (ii) Limitations period The Commission may seek restitution under this subparagraph not later than 5 years after the latest date on which the person from which the restitution is sought receives any unjust enrichment from the effects of the violation that gives rise to the suit in which the Commission seeks the restitution. (4) Rules of construction Nothing in this subsection may be construed as\u2014 (A) requiring the Commission to bring a suit seeking a temporary injunction under paragraph (1)(B) before bringing a suit seeking a permanent injunction under paragraph (1)(C); or (B) affecting the authority of the Federal Trade Commission under any other provision of law. .\n##### (b) Applicability\nSection 27 of the Federal Trade Commission Act, as added by subsection (a), shall apply with respect to any\u2014\n**(1)**\nconduct that occurs on or after the date of enactment of this Act; and\n**(2)**\naction or proceeding that is commenced on or after the date of enactment of this Act.\n##### (c) Antitrust laws\nExcept to the extent subsection (a) establishes an additional basis for liability under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ), nothing in this section, or the amendments made by this section, shall modify, impair, limit, or supersede the applicability of the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ), or of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that it applies to unfair methods of competition.\n##### (d) Rulemaking\nThe Federal Trade Commission may issue rules under section 553 of title 5, United States Code, to define any terms used in section 27 of the Federal Trade Commission Act, as added by subsection (a) (other than terms that are defined in subsection (a) of such section 27).",
      "versionDate": "2025-04-10",
      "versionType": "Reported in Senate"
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
            "name": "Administrative remedies",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-07T15:31:56Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-07T15:31:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-04T14:00:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1040",
          "measure-number": "1040",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2026-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1040v00",
            "update-date": "2026-01-30"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Drug Competition Enhancement Act </strong></p><p>This bill prohibits product hopping by drug manufacturers and authorizes the Federal Trade Commission (FTC) to enforce this prohibition.</p><p>Generally, <em>product\u00a0hopping</em> describes a situation where, when the patents on a reference drug (or biological product) expire, the manufacturer switches to a follow-on product that is covered by a later-expiring patent. Under this bill, a <em>follow-on product</em> is a modified version of the reference drug that has an indication (what the drug is used for) that is identical or substantively similar to an indication of the reference drug.</p><p>The bill establishes a presumption that product hopping has occurred when a reference drug manufacturer, after receiving notice that the Food and Drug Administration has received an application to market a competing generic (or biosimilar) version, takes certain actions such as withdrawing the reference drug from the market and selling a follow-on product.</p><p>A drug manufacturer may rebut these presumptions by demonstrating that its conduct was not intended to limit competition.</p><p>The bill makes product hopping an unfair method of competition and provides for enforcement by the FTC. If the FTC has reason to believe a manufacturer has violated or is about to violate this prohibition on product hopping, the FTC may institute an administrative proceeding or bring suit in federal court to stop the manufacturer\u2019s action and seek equitable remedies, including disgorgement of unjust profits or paying restitution to those harmed.\u00a0</p>"
        },
        "title": "Drug Competition Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1040.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Drug Competition Enhancement Act </strong></p><p>This bill prohibits product hopping by drug manufacturers and authorizes the Federal Trade Commission (FTC) to enforce this prohibition.</p><p>Generally, <em>product\u00a0hopping</em> describes a situation where, when the patents on a reference drug (or biological product) expire, the manufacturer switches to a follow-on product that is covered by a later-expiring patent. Under this bill, a <em>follow-on product</em> is a modified version of the reference drug that has an indication (what the drug is used for) that is identical or substantively similar to an indication of the reference drug.</p><p>The bill establishes a presumption that product hopping has occurred when a reference drug manufacturer, after receiving notice that the Food and Drug Administration has received an application to market a competing generic (or biosimilar) version, takes certain actions such as withdrawing the reference drug from the market and selling a follow-on product.</p><p>A drug manufacturer may rebut these presumptions by demonstrating that its conduct was not intended to limit competition.</p><p>The bill makes product hopping an unfair method of competition and provides for enforcement by the FTC. If the FTC has reason to believe a manufacturer has violated or is about to violate this prohibition on product hopping, the FTC may institute an administrative proceeding or bring suit in federal court to stop the manufacturer\u2019s action and seek equitable remedies, including disgorgement of unjust profits or paying restitution to those harmed.\u00a0</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1040"
    },
    "title": "Drug Competition Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Drug Competition Enhancement Act </strong></p><p>This bill prohibits product hopping by drug manufacturers and authorizes the Federal Trade Commission (FTC) to enforce this prohibition.</p><p>Generally, <em>product\u00a0hopping</em> describes a situation where, when the patents on a reference drug (or biological product) expire, the manufacturer switches to a follow-on product that is covered by a later-expiring patent. Under this bill, a <em>follow-on product</em> is a modified version of the reference drug that has an indication (what the drug is used for) that is identical or substantively similar to an indication of the reference drug.</p><p>The bill establishes a presumption that product hopping has occurred when a reference drug manufacturer, after receiving notice that the Food and Drug Administration has received an application to market a competing generic (or biosimilar) version, takes certain actions such as withdrawing the reference drug from the market and selling a follow-on product.</p><p>A drug manufacturer may rebut these presumptions by demonstrating that its conduct was not intended to limit competition.</p><p>The bill makes product hopping an unfair method of competition and provides for enforcement by the FTC. If the FTC has reason to believe a manufacturer has violated or is about to violate this prohibition on product hopping, the FTC may institute an administrative proceeding or bring suit in federal court to stop the manufacturer\u2019s action and seek equitable remedies, including disgorgement of unjust profits or paying restitution to those harmed.\u00a0</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1040"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1040is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1040rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Drug Competition Enhancement Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "title": "Drug Competition Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Drug Competition Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Trade Commission Act to prohibit product hopping, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:29Z"
    }
  ]
}
```
