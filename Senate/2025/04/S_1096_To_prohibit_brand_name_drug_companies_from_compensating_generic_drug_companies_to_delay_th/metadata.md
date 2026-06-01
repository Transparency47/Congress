# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1096?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1096
- Title: Preserve Access to Affordable Generics and Biosimilars Act
- Congress: 119
- Bill type: S
- Bill number: 1096
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2026-01-30T20:47:11Z
- Update date including text: 2026-01-30T20:47:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 46.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 46.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1096",
    "number": "1096",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Preserve Access to Affordable Generics and Biosimilars Act",
    "type": "S",
    "updateDate": "2026-01-30T20:47:11Z",
    "updateDateIncludingText": "2026-01-30T20:47:11Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 46.",
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
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
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
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
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
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
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
            "date": "2025-04-10T20:23:43Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-03T14:15:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-24T21:53:22Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
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
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "ND"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "VT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1096is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1096\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Klobuchar (for herself, Mr. Grassley , Mr. Durbin , Mr. Cramer , Mr. Blumenthal , Ms. Ernst , Mr. Welch , Mr. Kelly , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit brand name drug companies from compensating generic drug companies to delay the entry of a generic drug into the market, and to prohibit biological product manufacturers from compensating biosimilar and interchangeable companies to delay the entry of biosimilar biological products and interchangeable biological products.\n#### 1. Short title\nThis Act may be cited as the Preserve Access to Affordable Generics and Biosimilars Act .\n#### 2. Congressional findings and declaration of purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIn 1984, the Drug Price Competition and Patent Term Restoration Act ( Public Law 98\u2013417 ) (referred to in this Act as the 1984 Act ), was enacted with the intent of facilitating the early entry of generic drugs while preserving incentives for innovation.\n**(2)**\nPrescription drugs make up approximately 11 percent of the national health care spending.\n**(3)**\nInitially, the 1984 Act was successful in facilitating generic competition to the benefit of consumers and health care payers. Although 91 percent of all prescriptions dispensed in the United States are generic drugs, they account for only 18 percent of all expenditures.\n**(4)**\nGeneric drugs cost substantially less than brand name drugs, with discounts off the brand price averaging 80 to 85 percent.\n**(5)**\nFederal dollars currently account for over 40 percent of the $449,700,000,000 spent on retail prescription drugs annually.\n**(6)**\n**(A)**\nIn recent years, the intent of the 1984 Act has been subverted by certain settlement agreements in which brand name companies transfer value to their potential generic competitors to settle claims that the generic company is infringing the branded company\u2019s patents.\n**(B)**\nThese reverse payment settlement agreements\u2014\n**(i)**\nallow a branded company to share its monopoly profits with the generic company as a way to protect the branded company\u2019s monopoly; and\n**(ii)**\nhave unduly delayed the marketing of low-cost generic drugs contrary to free competition, the interests of consumers, and the principles underlying antitrust law.\n**(C)**\nBecause of the price disparity between brand name and generic drugs, such agreements are more profitable for both the brand and generic manufacturers than competition and will become increasingly common unless prohibited.\n**(D)**\nThese agreements result in consumers losing the benefits that the 1984 Act was intended to provide.\n**(7)**\nIn 2010, the Biologics Price Competition and Innovation Act ( Public Law 111\u2013148 ) (referred to in this Act as the BPCIA ), was enacted with the intent of facilitating the early entry of biosimilar and interchangeable follow-on versions of branded biological products while preserving incentives for innovation.\n**(8)**\nBiological drugs play an important role in treating many serious illnesses, from cancers to genetic disorders. They are also expensive, representing more than half of all prescription drug spending.\n**(9)**\nCompetition from biosimilar and interchangeable biological products promises to lower drug costs and increase patient access to biological medicines. But reverse payment settlement agreements also threaten to delay the entry of biosimilar and interchangeable biological products, which would undermine the goals of BPCIA.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto enhance competition in the pharmaceutical market by stopping anticompetitive agreements between brand name and generic drug and biosimilar biological product manufacturers that limit, delay, or otherwise prevent competition from generic drugs and biosimilar biological products; and\n**(2)**\nto support the purpose and intent of antitrust law by prohibiting anticompetitive practices in the pharmaceutical industry that harm consumers.\n#### 3. Unlawful compensation for delay\n##### (a) In general\nThe Federal Trade Commission Act ( 15 U.S.C. 44 et seq. ) is amended by inserting after section 26 ( 15 U.S.C. 57c\u20132 ) the following:\n27. Preserving access to affordable generics and biosimilars (a) Prohibition (1) In general It shall be a violation of this section for a party to enter into, or be a participant to, an agreement, resolving or settling, on a final or interim basis, a patent claim in connection with the sale of a drug product or biological product, that has anticompetitive effects. (2) Treatment A violation of this section shall be treated as an unfair method of competition in violation of section 5(a)(1). (3) Presumption (A) In general Subject to subparagraph (B), an agreement described in paragraph (1) shall be presumed to have anticompetitive effects for purposes of such paragraph if\u2014 (i) an ANDA filer or a biosimilar biological product application filer receives anything of value, including an exclusive license; and (ii) the ANDA filer or biosimilar biological product application filer agrees to limit or forgo research, development, manufacturing, marketing, or sales of the ANDA product or biosimilar biological product, as applicable, for any period of time. (B) Exception Subparagraph (A) shall not apply if the parties to such agreement demonstrate by a preponderance of the evidence that\u2014 (i) the value described in subparagraph (A)(i) is compensation solely for other goods or services that the ANDA filer or biosimilar biological product application filer has promised to provide; or (ii) the procompetitive benefits of the transfer of value described in subparagraph (A)(i) and the agreement by the ANDA filer or biosimilar biological product application filer to limit or forgo research, development, manufacturing, marketing, or sales of the ANDA product or biosimilar biological product described in subparagraph (A)(ii) outweigh the anticompetitive effects of the transfer of value described in subparagraph (A)(i) and the agreement by the ANDA filer or biosimilar biological product application filer to limit or forgo research, development, manufacturing, marketing, or sales of the ANDA product or biosimilar biological product described in subparagraph (A)(ii). (4) Civil action In addition to any proceeding under section 5, if the Commission has reason to believe that a party has violated this section, the Commission may bring, in its own name by any of its attorneys designated by it for such purpose, a civil action against the party in a district court of the United States to seek to recover any of the remedies of civil penalty, mandatory injunctions, and such other and further equitable relief as the court deems appropriate. (5) Civil penalty (A) In general Each party that violates or assists in the violation of paragraph (1) shall forfeit and pay to the United States a civil penalty sufficient to deter violations of paragraph (1), but in no event greater than 3 times the value received by the party that is reasonably attributable to the violation of paragraph (1). If no such value has been received by the NDA holder, the biological product license holder, the ANDA filer, or the biosimilar biological product application filer, the penalty to the NDA holder, the biological product license holder, the ANDA filer, or the biosimilar biological product application filer shall be sufficient to deter violations, but in no event shall be greater than 3 times the value given to an ANDA filer or biosimilar biological product application filer reasonably attributable to the violation of this section. (B) Amount In determining the amount of the civil penalty described in subparagraph (A), the court shall take into account\u2014 (i) the nature, circumstances, extent, and gravity of the violation; (ii) with respect to the violator, the degree of culpability, any history of prior such conduct, including other agreements resolving or settling a patent infringement claim, the ability to pay, any effect on the ability to continue doing business, profits earned by the NDA holder, the biological product license holder, the ANDA filer, or the biosimilar biological product application filer, compensation received by the ANDA filer or biosimilar biological product application filer, and the amount of commerce affected; and (iii) other matters that justice requires. (C) Remedies in addition Remedies provided in this paragraph are in addition to, and not in lieu of, any other remedy provided by Federal law. Nothing in this section shall be construed to limit any authority of the Commission under any other provision of law. (b) Exclusions Nothing in this section shall prohibit a resolution or settlement of a patent infringement claim in which the consideration that the ANDA filer or biosimilar biological product application filer, respectively, receives as part of the resolution or settlement includes only one or more of the following: (1) The right to market and secure final approval in the United States for the ANDA product or biosimilar biological product at a date, whether certain or contingent, prior to the expiration of\u2014 (A) any patent that is the basis for the patent infringement claim; or (B) any patent right or other statutory exclusivity that would prevent the marketing of such ANDA product or biosimilar biological product. (2) A payment for reasonable litigation expenses not to exceed\u2014 (A) for calendar year 2025, $7,500,000; or (B) for calendar year 2026 and each subsequent calendar year, the amount determined for the preceding calendar year adjusted to reflect the percentage increase (if any) in the Producer Price Index for Legal Services published by the Bureau of Labor Statistics of the Department of Labor for the most recent calendar year. (3) A covenant not to sue on any claim that the ANDA product or biosimilar biological product infringes a United States patent. (c) Antitrust laws Except to the extent this section establishes an additional basis of liability, nothing in this section shall modify, impair, limit, or supersede the applicability of the antitrust laws as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12(a) ), and of section 5 of this Act to the extent that section 5 applies to unfair methods of competition. Nothing in this section shall modify, impair, limit, or supersede the right of an ANDA filer or biosimilar biological product application filer to assert claims or counterclaims against any person, under the antitrust laws or other laws relating to unfair competition. (d) Definitions In this section: (1) Agreement The term agreement means anything that would constitute an agreement under section 1 of the Sherman Act ( 15 U.S.C. 1 ) or section 5 of this Act. (2) Agreement resolving or settling a patent infringement claim The term agreement resolving or settling a patent infringement claim includes any agreement that is entered into within 30 days of the resolution or the settlement of the claim, or any other agreement that is contingent upon, provides a contingent condition for, or is otherwise related to the resolution or settlement of the claim. (3) ANDA The term ANDA means an abbreviated new drug application filed under section 505(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) ) or a new drug application submitted pursuant to section 505(b)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b)(2) ). (4) ANDA filer The term ANDA filer means a party that owns or controls an ANDA filed with the Secretary of Health and Human Services or has the exclusive rights under such ANDA to distribute the ANDA product. (5) ANDA product The term ANDA product means the product to be manufactured under the ANDA that is the subject of the patent infringement claim. (6) Biological product The term biological product has the meaning given such term in section 351(i)(1) of the Public Health Service Act ( 42 U.S.C. 262(i)(1) ). (7) Biological product license application The term biological product license application means an application under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ). (8) Biological product license holder The term biological product license holder means\u2014 (A) the holder of an approved biological product license application for a biological product; (B) a person owning or controlling enforcement of any patents that claim the biological product that is the subject of such approved application; or (C) the predecessors, subsidiaries, divisions, groups, and affiliates controlled by, controlling, or under common control with any of the entities described in subparagraphs (A) and (B) (such control to be presumed by direct or indirect share ownership of 50 percent or greater), as well as the licensees, licensors, successors, and assigns of each of the entities. (9) Biosimilar biological product The term biosimilar biological product means the product to be manufactured under the biosimilar biological product application that is the subject of the patent infringement claim. (10) Biosimilar biological product application The term biosimilar biological product application means an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) for licensure of a biological product as biosimilar to, or interchangeable with, a reference product. (11) Biosimilar biological product application filer The term biosimilar biological product application filer means a party that owns or controls a biosimilar biological product application filed with the Secretary of Health and Human Services or has the exclusive rights under such application to distribute the biosimilar biological product. (12) Drug product The term drug product has the meaning given such term in section 314.3(b) of title 21, Code of Federal Regulations (or any successor regulation). (13) Market The term market means the promotion, offering for sale, selling, or distribution of a drug product. (14) NDA The term NDA means a new drug application filed under section 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ). (15) NDA holder The term NDA holder means\u2014 (A) the holder of an approved NDA application for a drug product; (B) a person owning or controlling enforcement of the patent listed in the Approved Drug Products With Therapeutic Equivalence Evaluations (commonly known as the FDA Orange Book ) in connection with the NDA; or (C) the predecessors, subsidiaries, divisions, groups, and affiliates controlled by, controlling, or under common control with any of the entities described in subparagraphs (A) and (B) (such control to be presumed by direct or indirect share ownership of 50 percent or greater), as well as the licensees, licensors, successors, and assigns of each of the entities. (16) Party The term party means any person, partnership, corporation, or other legal entity. (17) Patent infringement The term patent infringement means infringement of any patent or of any filed patent application, including any extension, reissue, renewal, division, continuation, continuation in part, reexamination, patent term restoration, patents of addition, and extensions thereof. (18) Patent infringement claim The term patent infringement claim means any allegation made to an ANDA filer or biosimilar biological product application filer, whether or not included in a complaint filed with a court of law, that its ANDA or ANDA product, or biosimilar biological product application or biosimilar biological product, may infringe any patent held by, or exclusively licensed to, the NDA holder or biological product license holder of the drug product or biological product, as applicable. (19) Statutory exclusivity The term statutory exclusivity means those prohibitions on the submission or the approval of drug applications under clauses (ii) through (iv) of section 505(c)(3)(E), clauses (ii) through (iv) of section 505(j)(5)(F), section 527, section 505A, or section 505E of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c)(3)(E) , 360cc, 355a, 355f), or on the submission or licensing of biological product applications under section 351(k)(7) or paragraph (2) or (3) of section 351(m) of the Public Health Service Act ( 42 U.S.C. 262 ) or under section 527 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360cc ). .\n##### (b) Effective date\nSection 27 of the Federal Trade Commission Act, as added by this section, shall apply to all agreements described in section 27(a)(1) of that Act entered into on or after the date of enactment of this Act.\n#### 4. Certification of agreements\n##### (a) Notice of all agreements\nSection 1111(7) of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 21 U.S.C. 355 note) is amended by inserting , or the owner of a patent for which a claim of infringement could reasonably be asserted against any person for making, using, offering to sell, selling, or importing into the United States a biological product that is the subject of a biosimilar biological product application before the period at the end.\n##### (b) Certification of agreements\nSection 1112 of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 21 U.S.C. 355 note) is amended by adding at the end the following:\n(d) Certification The Chief Executive Officer or the company official responsible for negotiating any agreement under subsection (a) or (b) that is required to be filed under subsection (c), within 30 days after such filing, shall execute and file with the Assistant Attorney General and the Commission a certification as follows: \u2018I declare that the following is true, correct, and complete to the best of my knowledge: The materials filed with the Federal Trade Commission and the Department of Justice under section 1112 of subtitle B of title XI of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003, with respect to the agreement referenced in this certification\u2014 (1) represent the complete, final, and exclusive agreement between the parties; (2) include any ancillary agreements that are contingent upon, provide a contingent condition for, or are otherwise related to, the referenced agreement; and (3) include written descriptions of any oral agreements, representations, commitments, or promises between the parties that are responsive to subsection (a) or (b) of such section 1112 and have not been reduced to writing.\u2019 .\n#### 5. Notification of agreements\nSection 1112 of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 21 U.S.C. 355 note), as amended by section 4(b), is further amended by adding at the end the following:\n(e) Rule of construction (1) In general An agreement that is required under subsection (a) or (b) shall include agreements resolving any outstanding disputes, including agreements resolving or settling a Patent Trial and Appeal Board proceeding. (2) Definition For purposes of subparagraph (A), the term Patent Trial and Appeal Board proceeding means a proceeding conducted by the Patent Trial and Appeal Board of the United States Patent and Trademark Office, including an inter partes review instituted under chapter 31 of title 35, United States Code, a post-grant review instituted under chapter 32 of that title (including a proceeding instituted pursuant to the transitional program for covered business method patents, as described in section 18 of the Leahy-Smith America Invents Act ( 35 U.S.C. 321 note)), and a derivation proceeding instituted under section 135 of that title. .\n#### 6. Forfeiture of 180 -day exclusivity period\nSection 505(j)(5)(D)(i)(V) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(5)(D)(i)(V) ) is amended by inserting section 27 of the Federal Trade Commission Act or after that the agreement has violated .\n#### 7. Commission litigation authority\nSection 16(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 56(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (D), by striking or after the semicolon;\n**(2)**\nin subparagraph (E)\u2014\n**(A)**\nby moving the margin 2 ems to the left; and\n**(B)**\nby inserting or after the semicolon; and\n**(3)**\ninserting after subparagraph (E) the following:\n(F) under section 27, .\n#### 8. Report on additional exclusion\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Federal Trade Commission shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a recommendation, and the Commission\u2019s basis for such recommendation, regarding a potential amendment to include in section 27(b) of the Federal Trade Commission Act (as added by section 3) an additional exclusion for consideration granted by an NDA holder to a ANDA filer or by a biological product license holder to a biosimilar biological product application filer as part of the resolution or settlement, a release, waiver, or limitation of a claim for damages or other monetary relief.\n**(2) Definitions**\nIn this section, the terms ANDA filer , biological product license holder , biosimilar biological product application filer , and NDA holder have the meanings given such terms in section 27(d) of the Federal Trade Commission Act (as added by section 3).\n#### 9. Statute of limitations\nThe Federal Trade Commission shall commence any enforcement proceeding described in section 27 of the Federal Trade Commission Act, as added by section 3, not later than 6 years after the date on which the parties to the agreement file the certification under section 1112(d) of the Medicare Prescription Drug Improvement and Modernization Act of 2003 ( 21 U.S.C. 355 note).\n#### 10. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of the provisions of such Act or amendments to any person or circumstance shall not be affected.",
      "versionDate": "2025-03-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1096rs.xml",
      "text": "II\nCalendar No. 46\n119th CONGRESS\n1st Session\nS. 1096\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Klobuchar (for herself, Mr. Grassley , Mr. Durbin , Mr. Cramer , Mr. Blumenthal , Ms. Ernst , Mr. Welch , Mr. Kelly , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 10, 2025 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo prohibit brand name drug companies from compensating generic drug companies to delay the entry of a generic drug into the market, and to prohibit biological product manufacturers from compensating biosimilar and interchangeable companies to delay the entry of biosimilar biological products and interchangeable biological products.\n#### 1. Short title\nThis Act may be cited as the Preserve Access to Affordable Generics and Biosimilars Act .\n#### 2. Congressional findings and declaration of purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIn 1984, the Drug Price Competition and Patent Term Restoration Act ( Public Law 98\u2013417 ) (referred to in this Act as the 1984 Act ), was enacted with the intent of facilitating the early entry of generic drugs while preserving incentives for innovation.\n**(2)**\nPrescription drugs make up approximately 11 percent of the national health care spending.\n**(3)**\nInitially, the 1984 Act was successful in facilitating generic competition to the benefit of consumers and health care payers. Although 91 percent of all prescriptions dispensed in the United States are generic drugs, they account for only 18 percent of all expenditures.\n**(4)**\nGeneric drugs cost substantially less than brand name drugs, with discounts off the brand price averaging 80 to 85 percent.\n**(5)**\nFederal dollars currently account for over 40 percent of the $449,700,000,000 spent on retail prescription drugs annually.\n**(6)**\n**(A)**\nIn recent years, the intent of the 1984 Act has been subverted by certain settlement agreements in which brand name companies transfer value to their potential generic competitors to settle claims that the generic company is infringing the branded company\u2019s patents.\n**(B)**\nThese reverse payment settlement agreements\u2014\n**(i)**\nallow a branded company to share its monopoly profits with the generic company as a way to protect the branded company\u2019s monopoly; and\n**(ii)**\nhave unduly delayed the marketing of low-cost generic drugs contrary to free competition, the interests of consumers, and the principles underlying antitrust law.\n**(C)**\nBecause of the price disparity between brand name and generic drugs, such agreements are more profitable for both the brand and generic manufacturers than competition and will become increasingly common unless prohibited.\n**(D)**\nThese agreements result in consumers losing the benefits that the 1984 Act was intended to provide.\n**(7)**\nIn 2010, the Biologics Price Competition and Innovation Act ( Public Law 111\u2013148 ) (referred to in this Act as the BPCIA ), was enacted with the intent of facilitating the early entry of biosimilar and interchangeable follow-on versions of branded biological products while preserving incentives for innovation.\n**(8)**\nBiological drugs play an important role in treating many serious illnesses, from cancers to genetic disorders. They are also expensive, representing more than half of all prescription drug spending.\n**(9)**\nCompetition from biosimilar and interchangeable biological products promises to lower drug costs and increase patient access to biological medicines. But reverse payment settlement agreements also threaten to delay the entry of biosimilar and interchangeable biological products, which would undermine the goals of BPCIA.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto enhance competition in the pharmaceutical market by stopping anticompetitive agreements between brand name and generic drug and biosimilar biological product manufacturers that limit, delay, or otherwise prevent competition from generic drugs and biosimilar biological products; and\n**(2)**\nto support the purpose and intent of antitrust law by prohibiting anticompetitive practices in the pharmaceutical industry that harm consumers.\n#### 3. Unlawful compensation for delay\n##### (a) In general\nThe Federal Trade Commission Act ( 15 U.S.C. 44 et seq. ) is amended by inserting after section 26 ( 15 U.S.C. 57c\u20132 ) the following:\n27. Preserving access to affordable generics and biosimilars (a) Prohibition (1) In general It shall be a violation of this section for a party to enter into, or be a participant to, an agreement, resolving or settling, on a final or interim basis, a patent claim in connection with the sale of a drug product or biological product, that has anticompetitive effects. (2) Treatment A violation of this section shall be treated as an unfair method of competition in violation of section 5(a)(1). (3) Presumption (A) In general Subject to subparagraph (B), an agreement described in paragraph (1) shall be presumed to have anticompetitive effects for purposes of such paragraph if\u2014 (i) an ANDA filer or a biosimilar biological product application filer receives anything of value, including an exclusive license; and (ii) the ANDA filer or biosimilar biological product application filer agrees to limit or forgo research, development, manufacturing, marketing, or sales of the ANDA product or biosimilar biological product, as applicable, for any period of time. (B) Exception Subparagraph (A) shall not apply if the parties to such agreement demonstrate by a preponderance of the evidence that\u2014 (i) the value described in subparagraph (A)(i) is compensation solely for other goods or services that the ANDA filer or biosimilar biological product application filer has promised to provide; or (ii) the procompetitive benefits of the transfer of value described in subparagraph (A)(i) and the agreement by the ANDA filer or biosimilar biological product application filer to limit or forgo research, development, manufacturing, marketing, or sales of the ANDA product or biosimilar biological product described in subparagraph (A)(ii) outweigh the anticompetitive effects of the transfer of value described in subparagraph (A)(i) and the agreement by the ANDA filer or biosimilar biological product application filer to limit or forgo research, development, manufacturing, marketing, or sales of the ANDA product or biosimilar biological product described in subparagraph (A)(ii). (4) Civil action In addition to any proceeding under section 5, if the Commission has reason to believe that a party has violated this section, the Commission may bring, in its own name by any of its attorneys designated by it for such purpose, a civil action against the party in a district court of the United States to seek to recover any of the remedies of civil penalty, mandatory injunctions, and such other and further equitable relief as the court deems appropriate. (5) Civil penalty (A) In general Each party that violates or assists in the violation of paragraph (1) shall forfeit and pay to the United States a civil penalty sufficient to deter violations of paragraph (1), but in no event greater than 3 times the value received by the party that is reasonably attributable to the violation of paragraph (1). If no such value has been received by the NDA holder, the biological product license holder, the ANDA filer, or the biosimilar biological product application filer, the penalty to the NDA holder, the biological product license holder, the ANDA filer, or the biosimilar biological product application filer shall be sufficient to deter violations, but in no event shall be greater than 3 times the value given to an ANDA filer or biosimilar biological product application filer reasonably attributable to the violation of this section. (B) Amount In determining the amount of the civil penalty described in subparagraph (A), the court shall take into account\u2014 (i) the nature, circumstances, extent, and gravity of the violation; (ii) with respect to the violator, the degree of culpability, any history of prior such conduct, including other agreements resolving or settling a patent infringement claim, the ability to pay, any effect on the ability to continue doing business, profits earned by the NDA holder, the biological product license holder, the ANDA filer, or the biosimilar biological product application filer, compensation received by the ANDA filer or biosimilar biological product application filer, and the amount of commerce affected; and (iii) other matters that justice requires. (C) Remedies in addition Remedies provided in this paragraph are in addition to, and not in lieu of, any other remedy provided by Federal law. Nothing in this section shall be construed to limit any authority of the Commission under any other provision of law. (b) Exclusions Nothing in this section shall prohibit a resolution or settlement of a patent infringement claim in which the consideration that the ANDA filer or biosimilar biological product application filer, respectively, receives as part of the resolution or settlement includes only one or more of the following: (1) The right to market and secure final approval in the United States for the ANDA product or biosimilar biological product at a date, whether certain or contingent, prior to the expiration of\u2014 (A) any patent that is the basis for the patent infringement claim; or (B) any patent right or other statutory exclusivity that would prevent the marketing of such ANDA product or biosimilar biological product. (2) A payment for reasonable litigation expenses not to exceed\u2014 (A) for calendar year 2025, $7,500,000; or (B) for calendar year 2026 and each subsequent calendar year, the amount determined for the preceding calendar year adjusted to reflect the percentage increase (if any) in the Producer Price Index for Legal Services published by the Bureau of Labor Statistics of the Department of Labor for the most recent calendar year. (3) A covenant not to sue on any claim that the ANDA product or biosimilar biological product infringes a United States patent. (c) Antitrust laws Except to the extent this section establishes an additional basis of liability, nothing in this section shall modify, impair, limit, or supersede the applicability of the antitrust laws as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12(a) ), and of section 5 of this Act to the extent that section 5 applies to unfair methods of competition. Nothing in this section shall modify, impair, limit, or supersede the right of an ANDA filer or biosimilar biological product application filer to assert claims or counterclaims against any person, under the antitrust laws or other laws relating to unfair competition. (d) Definitions In this section: (1) Agreement The term agreement means anything that would constitute an agreement under section 1 of the Sherman Act ( 15 U.S.C. 1 ) or section 5 of this Act. (2) Agreement resolving or settling a patent infringement claim The term agreement resolving or settling a patent infringement claim includes any agreement that is entered into within 30 days of the resolution or the settlement of the claim, or any other agreement that is contingent upon, provides a contingent condition for, or is otherwise related to the resolution or settlement of the claim. (3) ANDA The term ANDA means an abbreviated new drug application filed under section 505(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) ) or a new drug application submitted pursuant to section 505(b)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b)(2) ). (4) ANDA filer The term ANDA filer means a party that owns or controls an ANDA filed with the Secretary of Health and Human Services or has the exclusive rights under such ANDA to distribute the ANDA product. (5) ANDA product The term ANDA product means the product to be manufactured under the ANDA that is the subject of the patent infringement claim. (6) Biological product The term biological product has the meaning given such term in section 351(i)(1) of the Public Health Service Act ( 42 U.S.C. 262(i)(1) ). (7) Biological product license application The term biological product license application means an application under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ). (8) Biological product license holder The term biological product license holder means\u2014 (A) the holder of an approved biological product license application for a biological product; (B) a person owning or controlling enforcement of any patents that claim the biological product that is the subject of such approved application; or (C) the predecessors, subsidiaries, divisions, groups, and affiliates controlled by, controlling, or under common control with any of the entities described in subparagraphs (A) and (B) (such control to be presumed by direct or indirect share ownership of 50 percent or greater), as well as the licensees, licensors, successors, and assigns of each of the entities. (9) Biosimilar biological product The term biosimilar biological product means the product to be manufactured under the biosimilar biological product application that is the subject of the patent infringement claim. (10) Biosimilar biological product application The term biosimilar biological product application means an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) for licensure of a biological product as biosimilar to, or interchangeable with, a reference product. (11) Biosimilar biological product application filer The term biosimilar biological product application filer means a party that owns or controls a biosimilar biological product application filed with the Secretary of Health and Human Services or has the exclusive rights under such application to distribute the biosimilar biological product. (12) Drug product The term drug product has the meaning given such term in section 314.3(b) of title 21, Code of Federal Regulations (or any successor regulation). (13) Market The term market means the promotion, offering for sale, selling, or distribution of a drug product. (14) NDA The term NDA means a new drug application filed under section 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ). (15) NDA holder The term NDA holder means\u2014 (A) the holder of an approved NDA application for a drug product; (B) a person owning or controlling enforcement of the patent listed in the Approved Drug Products With Therapeutic Equivalence Evaluations (commonly known as the FDA Orange Book ) in connection with the NDA; or (C) the predecessors, subsidiaries, divisions, groups, and affiliates controlled by, controlling, or under common control with any of the entities described in subparagraphs (A) and (B) (such control to be presumed by direct or indirect share ownership of 50 percent or greater), as well as the licensees, licensors, successors, and assigns of each of the entities. (16) Party The term party means any person, partnership, corporation, or other legal entity. (17) Patent infringement The term patent infringement means infringement of any patent or of any filed patent application, including any extension, reissue, renewal, division, continuation, continuation in part, reexamination, patent term restoration, patents of addition, and extensions thereof. (18) Patent infringement claim The term patent infringement claim means any allegation made to an ANDA filer or biosimilar biological product application filer, whether or not included in a complaint filed with a court of law, that its ANDA or ANDA product, or biosimilar biological product application or biosimilar biological product, may infringe any patent held by, or exclusively licensed to, the NDA holder or biological product license holder of the drug product or biological product, as applicable. (19) Statutory exclusivity The term statutory exclusivity means those prohibitions on the submission or the approval of drug applications under clauses (ii) through (iv) of section 505(c)(3)(E), clauses (ii) through (iv) of section 505(j)(5)(F), section 527, section 505A, or section 505E of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c)(3)(E) , 360cc, 355a, 355f), or on the submission or licensing of biological product applications under section 351(k)(7) or paragraph (2) or (3) of section 351(m) of the Public Health Service Act ( 42 U.S.C. 262 ) or under section 527 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360cc ). .\n##### (b) Effective date\nSection 27 of the Federal Trade Commission Act, as added by this section, shall apply to all agreements described in section 27(a)(1) of that Act entered into on or after the date of enactment of this Act.\n#### 4. Certification of agreements\n##### (a) Notice of all agreements\nSection 1111(7) of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 21 U.S.C. 355 note) is amended by inserting , or the owner of a patent for which a claim of infringement could reasonably be asserted against any person for making, using, offering to sell, selling, or importing into the United States a biological product that is the subject of a biosimilar biological product application before the period at the end.\n##### (b) Certification of agreements\nSection 1112 of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 21 U.S.C. 355 note) is amended by adding at the end the following:\n(d) Certification The Chief Executive Officer or the company official responsible for negotiating any agreement under subsection (a) or (b) that is required to be filed under subsection (c), within 30 days after such filing, shall execute and file with the Assistant Attorney General and the Commission a certification as follows: \u2018I declare that the following is true, correct, and complete to the best of my knowledge: The materials filed with the Federal Trade Commission and the Department of Justice under section 1112 of subtitle B of title XI of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003, with respect to the agreement referenced in this certification\u2014 (1) represent the complete, final, and exclusive agreement between the parties; (2) include any ancillary agreements that are contingent upon, provide a contingent condition for, or are otherwise related to, the referenced agreement; and (3) include written descriptions of any oral agreements, representations, commitments, or promises between the parties that are responsive to subsection (a) or (b) of such section 1112 and have not been reduced to writing.\u2019 .\n#### 5. Notification of agreements\nSection 1112 of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 21 U.S.C. 355 note), as amended by section 4(b), is further amended by adding at the end the following:\n(e) Rule of construction (1) In general An agreement that is required under subsection (a) or (b) shall include agreements resolving any outstanding disputes, including agreements resolving or settling a Patent Trial and Appeal Board proceeding. (2) Definition For purposes of subparagraph (A), the term Patent Trial and Appeal Board proceeding means a proceeding conducted by the Patent Trial and Appeal Board of the United States Patent and Trademark Office, including an inter partes review instituted under chapter 31 of title 35, United States Code, a post-grant review instituted under chapter 32 of that title (including a proceeding instituted pursuant to the transitional program for covered business method patents, as described in section 18 of the Leahy-Smith America Invents Act ( 35 U.S.C. 321 note)), and a derivation proceeding instituted under section 135 of that title. .\n#### 6. Forfeiture of 180 -day exclusivity period\nSection 505(j)(5)(D)(i)(V) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(5)(D)(i)(V) ) is amended by inserting section 27 of the Federal Trade Commission Act or after that the agreement has violated .\n#### 7. Commission litigation authority\nSection 16(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 56(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (D), by striking or after the semicolon;\n**(2)**\nin subparagraph (E)\u2014\n**(A)**\nby moving the margin 2 ems to the left; and\n**(B)**\nby inserting or after the semicolon; and\n**(3)**\ninserting after subparagraph (E) the following:\n(F) under section 27, .\n#### 8. Report on additional exclusion\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Federal Trade Commission shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a recommendation, and the Commission\u2019s basis for such recommendation, regarding a potential amendment to include in section 27(b) of the Federal Trade Commission Act (as added by section 3) an additional exclusion for consideration granted by an NDA holder to a ANDA filer or by a biological product license holder to a biosimilar biological product application filer as part of the resolution or settlement, a release, waiver, or limitation of a claim for damages or other monetary relief.\n**(2) Definitions**\nIn this section, the terms ANDA filer , biological product license holder , biosimilar biological product application filer , and NDA holder have the meanings given such terms in section 27(d) of the Federal Trade Commission Act (as added by section 3).\n#### 9. Statute of limitations\nThe Federal Trade Commission shall commence any enforcement proceeding described in section 27 of the Federal Trade Commission Act, as added by section 3, not later than 6 years after the date on which the parties to the agreement file the certification under section 1112(d) of the Medicare Prescription Drug Improvement and Modernization Act of 2003 ( 21 U.S.C. 355 note).\n#### 10. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of the provisions of such Act or amendments to any person or circumstance shall not be affected.",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Contracts and agency",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-04-07T15:50:20Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-07T15:50:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-04T13:36:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119s1096",
          "measure-number": "1096",
          "measure-type": "s",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2026-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1096v00",
            "update-date": "2026-01-30"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Preserve Access to Affordable Generics and Biosimilars Act</strong></p><p>This bill prohibits parties from entering into any agreement that resolves or settles a patent claim related to the sale of a drug or biological product and that has anticompetitive effects. Such an agreement is presumed to have anticompetitive effects if the filer of a generic drug or biosimilar application receives anything of value and agrees to limit or forego research, development, manufacturing, marketing, or sales of the generic drug or biosimilar.</p><p>An agreement is exempt if the only consideration granted to the generic manufacturer is (1) the right to market and secure final approval for its product prior to the expiration of any statutory exclusivity, (2) a payment for reasonable litigation expenses, or (3) a covenant not to sue on any claim that the generic drug or biosimilar infringes a U.S. patent. An agreement is also exempt if the agreement's pro-competitive benefits outweigh the anticompetitive effects.</p><p>The bill provides for enforcement by the Federal Trade Commission (FTC). Violators are subject to penalties including\u00a0the forfeiture of the 180-day marketing exclusivity period for a generic drug.</p><p>Additionally, when a generic or biosimilar drug manufacturer enters into an agreement with another drug manufacturer related to the manufacturing, marketing, or sale of a drug, the manufacturers must certify that the material they have given the FTC and the Department of Justice concerning the agreement contains the complete agreement and any related agreements, including descriptions of any oral agreements or representations.</p>"
        },
        "title": "Preserve Access to Affordable Generics and Biosimilars Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1096.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preserve Access to Affordable Generics and Biosimilars Act</strong></p><p>This bill prohibits parties from entering into any agreement that resolves or settles a patent claim related to the sale of a drug or biological product and that has anticompetitive effects. Such an agreement is presumed to have anticompetitive effects if the filer of a generic drug or biosimilar application receives anything of value and agrees to limit or forego research, development, manufacturing, marketing, or sales of the generic drug or biosimilar.</p><p>An agreement is exempt if the only consideration granted to the generic manufacturer is (1) the right to market and secure final approval for its product prior to the expiration of any statutory exclusivity, (2) a payment for reasonable litigation expenses, or (3) a covenant not to sue on any claim that the generic drug or biosimilar infringes a U.S. patent. An agreement is also exempt if the agreement's pro-competitive benefits outweigh the anticompetitive effects.</p><p>The bill provides for enforcement by the Federal Trade Commission (FTC). Violators are subject to penalties including\u00a0the forfeiture of the 180-day marketing exclusivity period for a generic drug.</p><p>Additionally, when a generic or biosimilar drug manufacturer enters into an agreement with another drug manufacturer related to the manufacturing, marketing, or sale of a drug, the manufacturers must certify that the material they have given the FTC and the Department of Justice concerning the agreement contains the complete agreement and any related agreements, including descriptions of any oral agreements or representations.</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1096"
    },
    "title": "Preserve Access to Affordable Generics and Biosimilars Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preserve Access to Affordable Generics and Biosimilars Act</strong></p><p>This bill prohibits parties from entering into any agreement that resolves or settles a patent claim related to the sale of a drug or biological product and that has anticompetitive effects. Such an agreement is presumed to have anticompetitive effects if the filer of a generic drug or biosimilar application receives anything of value and agrees to limit or forego research, development, manufacturing, marketing, or sales of the generic drug or biosimilar.</p><p>An agreement is exempt if the only consideration granted to the generic manufacturer is (1) the right to market and secure final approval for its product prior to the expiration of any statutory exclusivity, (2) a payment for reasonable litigation expenses, or (3) a covenant not to sue on any claim that the generic drug or biosimilar infringes a U.S. patent. An agreement is also exempt if the agreement's pro-competitive benefits outweigh the anticompetitive effects.</p><p>The bill provides for enforcement by the Federal Trade Commission (FTC). Violators are subject to penalties including\u00a0the forfeiture of the 180-day marketing exclusivity period for a generic drug.</p><p>Additionally, when a generic or biosimilar drug manufacturer enters into an agreement with another drug manufacturer related to the manufacturing, marketing, or sale of a drug, the manufacturers must certify that the material they have given the FTC and the Department of Justice concerning the agreement contains the complete agreement and any related agreements, including descriptions of any oral agreements or representations.</p>",
      "updateDate": "2026-01-30",
      "versionCode": "id119s1096"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1096is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1096rs.xml"
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
      "title": "Preserve Access to Affordable Generics and Biosimilars Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "title": "Preserve Access to Affordable Generics and Biosimilars Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preserve Access to Affordable Generics and Biosimilars Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit brand name drug companies from compensating generic drug companies to delay the entry of a generic drug into the market, and to prohibit biological product manufacturers from compensating biosimilar and interchangeable companies to delay the entry of biosimilar biological products and interchangeable biological products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:46Z"
    }
  ]
}
```
