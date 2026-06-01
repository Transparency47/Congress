# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3345
- Title: PBM Price Transparency and Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 3345
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-29T12:03:18Z
- Update date including text: 2026-01-29T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3345",
    "number": "3345",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "PBM Price Transparency and Accountability Act",
    "type": "S",
    "updateDate": "2026-01-29T12:03:18Z",
    "updateDateIncludingText": "2026-01-29T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
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
            "date": "2025-12-04T17:37:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-04T17:37:26Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OR"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "SD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "RI"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "LA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "OK"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NV"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WY"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NM"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "GA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "KS"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "SC"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "WV"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "DE"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-05",
      "state": "ID"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3345is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3345\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Crapo (for himself, Mr. Wyden , Mr. Grassley , Mr. Bennet , Mr. Cornyn , Mr. Warner , Mr. Thune , Mr. Whitehouse , Mr. Cassidy , Ms. Hassan , Mr. Lankford , Ms. Cortez Masto , Mr. Daines , Ms. Smith , Mr. Barrasso , Mr. Luj\u00e1n , Mr. Tillis , Mr. Warnock , Mrs. Blackburn , Mr. Welch , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to ensure accurate payments to pharmacies under Medicaid and prevent the use of abusive spread pricing in Medicaid, and to assure pharmacy access and choice for Medicare beneficiaries and modernize and ensure PBM accountability under Medicare.\n#### 1. Short title\nThis Act may be cited as the PBM Price Transparency and Accountability Act .\n#### 2. Ensuring accurate payments to pharmacies under Medicaid and preventing the use of abusive spread pricing in Medicaid\n##### (a) Ensuring accurate payments to pharmacies under Medicaid\n**(1) In general**\nSection 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ) is amended\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nby redesignating clause (ii) as clause (iii); and\n**(ii)**\nby striking and after the semicolon at the end of clause (i) and all that precedes it through (1) and inserting the following:\n(1) Determining pharmacy actual acquisition costs The Secretary shall conduct a survey of retail community pharmacy drug prices and applicable non-retail pharmacy drug prices to determine national average drug acquisition cost benchmarks (as such term is defined by the Secretary) as follows: (A) Use of vendor The Secretary may contract services for\u2014 (i) with respect to retail community pharmacies, the determination of retail survey prices of the national average drug acquisition cost for covered outpatient drugs that represent a nationwide average of consumer purchase prices for such drugs, net of all discounts, rebates, and other price concessions (to the extent any information with respect to such discounts, rebates, and other price concessions is available) based on a monthly survey of such pharmacies; (ii) with respect to applicable non-retail pharmacies\u2014 (I) the determination of survey prices, separate from the survey prices described in clause (i), of the non-retail national average drug acquisition cost for covered outpatient drugs that represent a nationwide average of consumer purchase prices for such drugs, net of all discounts, rebates, and other price concessions (to the extent any information with respect to such discounts, rebates, and other price concessions is available) based on a monthly survey of such pharmacies; and (II) at the discretion of the Secretary, for each type of applicable non-retail pharmacy, the determination of survey prices, separate from the survey prices described in clause (i) or subclause (I) of this clause, of the national average drug acquisition cost for such type of pharmacy for covered outpatient drugs that represent a nationwide average of consumer purchase prices for such drugs, net of all discounts, rebates, and other price concessions (to the extent any information with respect to such discounts, rebates, and other price concessions is available) based on a monthly survey of such pharmacies; and ;\n**(B)**\nin subparagraph (B) of paragraph (1), by striking subparagraph (A)(ii) and inserting subparagraph (A)(iii) ;\n**(C)**\nin subparagraph (D) of paragraph (1), by striking clauses (ii) and (iii) and inserting the following:\n(ii) The vendor must update the Secretary no less often than monthly on the survey prices for covered outpatient drugs. (iii) The vendor must differentiate, in collecting and reporting survey data, for all cost information collected, whether a pharmacy is a retail community pharmacy or an applicable non-retail pharmacy, including whether such pharmacy is an affiliate (as defined in subsection (k)(13)), and, in the case of an applicable non-retail pharmacy, which type of applicable non-retail pharmacy it is using the relevant pharmacy type indicators included in the guidance required by subsection (a)(4)(A) of section 2 of the PBM Price Transparency and Accountability Act . ;\n**(D)**\nby adding at the end of paragraph (1) the following:\n(F) Survey reporting In order to meet the requirement of section 1902(a)(54), a State shall require that any retail community pharmacy or applicable non-retail pharmacy in the State that receives any payment, reimbursement, administrative fee, discount, rebate, or other price concession related to the dispensing of covered outpatient drugs to individuals receiving benefits under this title, regardless of whether such payment, reimbursement, administrative fee, discount, rebate, or other price concession is received from the State or a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)) directly or from a pharmacy benefit manager or another entity that has a contract with the State or a managed care entity or other specified entity (as so defined), shall respond to surveys conducted under this paragraph. (G) Survey information Information on national drug acquisition prices obtained under this paragraph shall be made publicly available in a form and manner to be determined by the Secretary and shall include at least the following: (i) The monthly response rate to the survey including a list of pharmacies not in compliance with subparagraph (F). (ii) The sampling methodology and number of pharmacies sampled monthly. (iii) Information on price concessions to pharmacies, including discounts, rebates, and other price concessions, to the extent that such information may be publicly released and has been collected by the Secretary as part of the survey. (H) Penalties (i) In general Subject to clauses (ii), (iii), and (iv), the Secretary shall enforce the provisions of this paragraph with respect to a pharmacy through the establishment of civil money penalties applicable to a retail community pharmacy or an applicable non-retail pharmacy. (ii) Basis for penalties The Secretary shall impose a civil money penalty established under this subparagraph on a retail community pharmacy or applicable non-retail pharmacy if\u2014 (I) the retail pharmacy or applicable non-retail pharmacy refuses or otherwise fails to respond to a request for information about prices in connection with a survey under this subsection; (II) knowingly provides false information in response to such a survey; or (III) otherwise fails to comply with the requirements established under this paragraph. (iii) Parameters for penalties (I) In general A civil money penalty established under this subparagraph may be assessed with respect to each violation, and with respect to each non-compliant retail community pharmacy (including a pharmacy that is part of a chain) or non-compliant applicable non-retail pharmacy (including a pharmacy that is part of a chain), in an amount not to exceed $100,000 for each such violation. (II) Considerations In determining the amount of a civil money penalty imposed under this subparagraph, the Secretary may consider the size, business structure, and type of pharmacy involved, as well as the type of violation and other relevant factors, as determined appropriate by the Secretary. (iv) Rule of application The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil money penalty under this subparagraph in the same manner as such provisions apply to a civil money penalty or proceeding under section 1128A(a). (I) Limitation on use of applicable non-retail pharmacy pricing information No State shall use pricing information reported by applicable non-retail pharmacies under subparagraph (A)(ii) to develop or inform payment methodologies for retail community pharmacies. ;\n**(E)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by inserting , including payment rates and methodologies for determining ingredient cost reimbursement under managed care entities or other specified entities (as such terms are defined in section 1903(m)(9)(D)), after under this title ; and\n**(ii)**\nin subparagraph (B), by inserting and the basis for such dispensing fees before the semicolon;\n**(F)**\nby redesignating paragraph (4) as paragraph (5);\n**(G)**\nby inserting after paragraph (3) the following new paragraph:\n(4) Oversight (A) In general The Inspector General of the Department of Health and Human Services shall conduct periodic studies of the survey data reported under this subsection, as appropriate, including with respect to substantial variations in acquisition costs or other applicable costs, as well as with respect to how internal transfer prices and related party transactions may influence the costs reported by pharmacies that are affiliates (as defined in subsection (k)(13)) or are owned by, controlled by, or related under a common ownership structure with a wholesaler, distributor, or other entity that acquires covered outpatient drugs relative to costs reported by pharmacies not affiliated with such entities. The Inspector General shall provide periodic updates to Congress on the results of such studies, as appropriate, in a manner that does not disclose trade secrets or other proprietary information. (B) Appropriation There is appropriated to the Inspector General of the Department of Health and Human Services, out of any money in the Treasury not otherwise appropriated, $5,000,000 for fiscal year 2026, to remain available until expended, to carry out this paragraph. ; and\n**(H)**\nin paragraph (5), as so redesignated\u2014\n**(i)**\nby inserting , and $9,000,000 for fiscal year 2026 and each fiscal year thereafter, after 2010 ; and\n**(ii)**\nby inserting Funds appropriated under this paragraph for fiscal year 2026 and any subsequent fiscal year shall remain available until expended. after the period.\n**(2) Definitions**\nSection 1927(k) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k) ) is amended\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking In the section and inserting In this section ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(12) Applicable non-retail pharmacy The term applicable non-retail pharmacy means a pharmacy that is licensed as a pharmacy by the State and that is not a retail community pharmacy, including a pharmacy that dispenses prescription medications to patients primarily through mail and specialty pharmacies. Such term does not include nursing home pharmacies, long-term care facility pharmacies, hospital pharmacies, clinics, charitable or not-for-profit pharmacies, government pharmacies, or low dispensing pharmacies (as defined by the Secretary). (13) Affiliate The term affiliate means any entity that is owned by, controlled by, or related under a common ownership structure with a pharmacy benefit manager or a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)). .\n**(3) Effective date**\n**(A) In general**\nSubject to subparagraph (B), the amendments made by this subsection shall take effect on the first day of the first quarter that begins on or after the date that is 6 months after the date of enactment of this Act.\n**(B) Delayed application to applicable non-retail pharmacies**\nThe pharmacy survey requirements established by the amendments to section 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ) made by this subsection shall apply to retail community pharmacies beginning on the effective date described in subparagraph (A), but shall not apply to applicable non-retail pharmacies until the first day of the first quarter that begins on or after the date that is 18 months after the date of enactment of this Act.\n**(4) Identification of applicable non-retail pharmacies**\n**(A) In general**\nNot later than January 1, 2027, the Secretary of Health and Human Services shall, in consultation with stakeholders as appropriate, publish guidance specifying pharmacies that meet the definition of applicable non-retail pharmacies (as such term is defined in subsection (k)(12) of section 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ), as added by paragraph (2)), and that will be subject to the survey requirements under subsection (f)(1) of such section, as amended by paragraph (1).\n**(B) Inclusion of pharmacy type indicators**\nThe guidance published under subparagraph (A) shall include pharmacy type indicators to distinguish between different types of applicable non-retail pharmacies, such as pharmacies that dispense prescriptions primarily through the mail and pharmacies that dispense prescriptions that require special handling or distribution. An applicable non-retail pharmacy may be identified through multiple pharmacy type indicators.\n**(5) Implementation**\n**(A) In general**\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by this subsection by program instruction or otherwise.\n**(B) Nonapplication of Administrative Procedure Act**\nImplementation of the amendments made by this subsection shall be exempt from the requirements of section 553 of title 5, United States Code.\n**(6) Nonapplication of paperwork reduction act**\nChapter 35 of title 44, United States Code, shall not apply to any data collection undertaken by the Secretary of Health and Human Services under section 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ), as amended by this subsection.\n##### (b) Preventing the use of abusive spread pricing in Medicaid\n**(1) In general**\nSection 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ) is amended\u2014\n**(A)**\nin subsection (e), by adding at the end the following new paragraph:\n(6) Transparent prescription drug pass-through pricing required (A) In general A contract between the State and a pharmacy benefit manager (referred to in this paragraph as a PBM ), or a contract between the State and a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D) and collectively referred to in this paragraph as the entity ) that includes provisions making the entity responsible for coverage of covered outpatient drugs dispensed to individuals enrolled with the entity, shall require that payment for such drugs and related administrative services (as applicable), including payments made by a PBM on behalf of the State or entity, is based on a transparent prescription drug pass-through pricing model under which\u2014 (i) any payment made by the entity or the PBM (as applicable) for such a drug\u2014 (I) is limited to\u2014 (aa) ingredient cost; and (bb) a professional dispensing fee that is not less than the professional dispensing fee that the State would pay if the State were making the payment directly in accordance with the State plan; (II) is passed through in its entirety (except as reduced under Federal or State laws and regulations in response to instances of waste, fraud, or abuse) by the entity or PBM to the pharmacy or provider that dispenses the drug; and (III) is made in a manner that is consistent with sections 447.502, 447.512, 447.514, and 447.518 of title 42, Code of Federal Regulations (or any successor regulation) as if such requirements applied directly to the entity or the PBM, except that any payment by the entity or the PBM for the ingredient cost of such drug purchased by a covered entity (as defined in subsection (a)(5)(B)) may exceed the actual acquisition cost (as defined in 447.502 of title 42, Code of Federal Regulations, or any successor regulation) for such drug if\u2014 (aa) such drug was subject to an agreement under section 340B of the Public Health Service Act; (bb) such payment for the ingredient cost of such drug does not exceed the maximum payment that would have been made by the entity or the PBM for the ingredient cost of such drug if such drug had not been purchased by such covered entity; and (cc) such covered entity reports to the Secretary (in a form and manner specified by the Secretary), on an annual basis and with respect to payments for the ingredient costs of such drugs so purchased by such covered entity that are in excess of the actual acquisition costs for such drugs, the aggregate amount of such excess; (ii) payment to the entity or the PBM (as applicable) for administrative services performed by the entity or PBM is limited to an administrative fee that reflects the fair market value (as defined by the Secretary) of such services; (iii) the entity or the PBM (as applicable) makes available to the State, and the Secretary upon request in a form and manner specified by the Secretary, all costs and payments related to covered outpatient drugs and accompanying administrative services (as described in clause (ii)) incurred, received, or made by the entity or the PBM, broken down (as specified by the Secretary), to the extent such costs and payments are attributable to an individual covered outpatient drug, by each such drug, including any ingredient costs, professional dispensing fees, administrative fees (as described in clause (ii)), post-sale and post-invoice fees, discounts, or related adjustments such as direct and indirect remuneration fees, and any and all other remuneration, as defined by the Secretary; and (iv) any form of spread pricing whereby any amount charged or claimed by the entity or the PBM (as applicable) that exceeds the amount paid to the pharmacies or providers on behalf of the State or entity, including any post-sale or post-invoice fees, discounts, or related adjustments such as direct and indirect remuneration fees or assessments, as defined by the Secretary (after allowing for an administrative fee as described in clause (ii)) is not allowable for purposes of claiming Federal matching payments under this title. (B) Publication of information The Secretary shall publish, not less frequently than on an annual basis and in a manner that does not disclose the identity of a particular covered entity or organization, information received by the Secretary pursuant to subparagraph (A)(iii)(III) that is broken out by State and by each of the following categories of covered entity within each such State: (i) Covered entities described in subparagraph (A) of section 340B(a)(4) of the Public Health Service Act. (ii) Covered entities described in subparagraphs (B) through (K) of such section. (iii) Covered entities described in subparagraph (L) of such section. (iv) Covered entities described in subparagraph (M) of such section. (v) Covered entities described in subparagraph (N) of such section. (vi) Covered entities described in subparagraph (O) of such section. ; and\n**(B)**\nin subsection (k), as amended by subsection (a)(2), by adding at the end the following new paragraph:\n(14) Pharmacy benefit manager The term pharmacy benefit manager means any person or entity that, either directly or through an intermediary, acts as a price negotiator or group purchaser on behalf of a State, managed care entity (as defined in section 1903(m)(9)(D)), or other specified entity (as so defined), or manages the prescription drug benefits provided by a State, managed care entity, or other specified entity, including the processing and payment of claims for prescription drugs, the performance of drug utilization review, the processing of drug prior authorization requests, the managing of appeals or grievances related to the prescription drug benefits, contracting with pharmacies, controlling the cost of covered outpatient drugs, or the provision of services related thereto. Such term includes any person or entity that acts as a price negotiator (with regard to payment amounts to pharmacies and providers for a covered outpatient drug or the net cost of the drug) or group purchaser on behalf of a State, managed care entity, or other specified entity or that carries out 1 or more of the other activities described in the preceding sentence, irrespective of whether such person or entity calls itself a pharmacy benefit manager. .\n**(2) Conforming amendments**\nSection 1903(m) of such Act ( 42 U.S.C. 1396b(m) ) is amended\u2014\n**(A)**\nin paragraph (2)(A)(xiii)\u2014\n**(i)**\nby striking and (III) and inserting (III) ;\n**(ii)**\nby inserting before the period at the end the following: , and (IV) if the contract includes provisions making the entity responsible for coverage of covered outpatient drugs, the entity shall comply with the requirements of section 1927(e)(6) ; and\n**(iii)**\nby moving the margin 2 ems to the left; and\n**(B)**\nby adding at the end the following new paragraph:\n(10) No payment shall be made under this title to a State with respect to expenditures incurred by the State for payment for services provided by an other specified entity (as defined in paragraph (9)(D)(iii)) unless such services are provided in accordance with a contract between the State and such entity which satisfies the requirements of paragraph (2)(A)(xiii). .\n**(3) Effective date**\nThe amendments made by this subsection shall apply to contracts between States and managed care entities, other specified entities, or pharmacy benefit managers that have an effective date beginning on or after the date that is 18 months after the date of enactment of this Act.\n**(4) Implementation**\n**(A) In general**\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by this subsection by program instruction or otherwise.\n**(B) Nonapplication of Administrative Procedure Act**\nImplementation of the amendments made by this subsection shall be exempt from the requirements of section 553 of title 5, United States Code.\n**(5) Nonapplication of Paperwork Reduction Act**\nChapter 35 of title 44, United States Code, shall not apply to any data collection undertaken by the Secretary of Health and Human Services under section 1927(e) of the Social Security Act ( 42 U.S.C. 1396r\u20138(e) ), as amended by this subsection.\n#### 3. Assuring pharmacy access and choice for Medicare beneficiaries and modernizing and ensuring PBM accountability under Medicare\n##### (a) Assuring pharmacy access and choice for medicare beneficiaries\n**(1) In general**\nSection 1860D\u20134(b)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(1) ) is amended by striking subparagraph (A) and inserting the following:\n(A) In general (i) Participation of any willing pharmacy A PDP sponsor offering a prescription drug plan shall permit any pharmacy that meets the standard contract terms and conditions under such plan to participate as a network pharmacy of such plan. (ii) Contract terms and conditions (I) In general Notwithstanding any other provision of law, for plan years beginning on or after January 1, 2028, in accordance with clause (i), contract terms and conditions offered by such PDP sponsor shall be reasonable and relevant according to standards established by the Secretary under subclause (II). (II) Standards Not later than the first Monday in April of 2027, the Secretary shall establish standards for reasonable and relevant contract terms and conditions for purposes of this clause. (III) Request for information Not later than April 1, 2026, for purposes of establishing the standards under subclause (II), the Secretary shall issue a request for information to seek input on trends in prescription drug plan and network pharmacy contract terms and conditions, current prescription drug plan and network pharmacy contracting practices, whether pharmacy reimbursement and dispensing fees paid by PDP sponsors to network pharmacies sufficiently cover the ingredient and operational costs of such pharmacies, the use and application of pharmacy quality measures by PDP sponsors for network pharmacies, PDP sponsor restrictions or limitations on the dispensing of covered part D drugs by network pharmacies (or any subsets of such pharmacies), PDP sponsor auditing practices for network pharmacies, areas in current regulations or program guidance related to contracting between prescription drug plans and network pharmacies requiring clarification or additional specificity, factors for consideration in determining the reasonableness and relevance of contract terms and conditions between prescription drug plans and network pharmacies, and other issues as determined appropriate by the Secretary. .\n**(2) Essential retail pharmacies**\nSection 1860D\u201342 of the Social Security Act ( 42 U.S.C. 1395w\u2013152 ) is amended by adding at the end the following new subsection:\n(e) Essential retail pharmacies (1) In general With respect to plan years beginning on or after January 1, 2028, the Secretary shall publish reports, at least once every 2 years until 2034, and periodically thereafter, that provide information, to the extent feasible, on\u2014 (A) trends in ingredient cost reimbursement, dispensing fees, incentive payments and other fees paid by PDP sponsors offering prescription drug plans and MA organizations offering MA\u2013PD plans under this part to essential retail pharmacies (as defined in paragraph (2)) with respect to the dispensing of covered part D drugs, including a comparison of such trends between essential retail pharmacies and pharmacies that are not essential retail pharmacies; (B) trends in amounts paid to PDP sponsors offering prescription drug plans and MA organizations offering MA\u2013PD plans under this part by essential retail pharmacies with respect to the dispensing of covered part D drugs, including a comparison of such trends between essential retail pharmacies and pharmacies that are not essential retail pharmacies; (C) trends in essential retail pharmacy participation in pharmacy networks and preferred pharmacy networks for prescription drug plans offered by PDP sponsors and MA\u2013PD plans offered by MA organizations under this part, including a comparison of such trends between essential retail pharmacies and pharmacies that are not essential retail pharmacies; (D) trends in the number of essential retail pharmacies, including variation in such trends by geographic region or other factors; (E) a comparison of cost-sharing for covered part D drugs dispensed by essential retail pharmacies that are network pharmacies for prescription drug plans offered by PDP sponsors and MA\u2013PD plans offered by MA organizations under this part and cost-sharing for covered part D drugs dispensed by other network pharmacies for such plans located in similar geographic areas that are not essential retail pharmacies; (F) a comparison of the volume of covered part D drugs dispensed by essential retail pharmacies that are network pharmacies for prescription drug plans offered by PDP sponsors and MA\u2013PD plans offered by MA organizations under this part and such volume of dispensing by network pharmacies for such plans located in similar geographic areas that are not essential retail pharmacies, including information on any patterns or trends in such comparison specific to certain types of covered part D drugs, such as generic drugs or drugs specified as specialty drugs by a PDP sponsor under a prescription drug plan or an MA organization under an MA\u2013PD plan; and (G) a comparison of the information described in subparagraphs (A) through (F) between essential retail pharmacies that are network pharmacies for prescription drug plans offered by PDP sponsors under this part and essential retail pharmacies that are network pharmacies for MA\u2013PD plans offered by MA organizations under this part. (2) Definition of essential retail pharmacy In this subsection, the term essential retail pharmacy means, with respect to a plan year, a retail pharmacy that\u2014 (A) is not a pharmacy that is an affiliate as defined in paragraph (4); and (B) is located in\u2014 (i) a rural area in which there is no other retail pharmacy within 10 miles, as determined by the Secretary; (ii) a suburban area in which there is no other retail pharmacy within 2 miles, as determined by the Secretary; or (iii) an urban area in which there is no other retail pharmacy within 1 mile, as determined by the Secretary. (3) List of essential retail pharmacies (A) Publication of list of essential retail pharmacies For each plan year (beginning with plan year 2028), the Secretary shall publish, on a publicly available internet website of the Centers for Medicare & Medicaid Services, a list of pharmacies that meet the criteria described in subparagraphs (A) and (B) of paragraph (2) to be considered an essential retail pharmacy. (B) Required submissions from pdp sponsors For each plan year (beginning with plan year 2028), each PDP sponsor offering a prescription drug plan and each MA organization offering an MA\u2013PD plan shall submit to the Secretary, for the purposes of determining retail pharmacies that meet the criterion specified in subparagraph (A) of paragraph (2), a list of retail pharmacies that are affiliates of such sponsor or organization, or are affiliates of a pharmacy benefit manager acting on behalf of such sponsor or organization, at a time, and in a form and manner, specified by the Secretary. (C) Reporting by pdp sponsors and ma organizations For each plan year beginning with plan year 2027, each PDP sponsor offering a prescription drug plan and each MA organization offering an MA\u2013PD plan under this part shall submit to the Secretary information on incentive payments and other fees paid by such sponsor or organization to pharmacies, insofar as any such payments or fees are not otherwise reported, at a time, and in a form and manner, specified by the Secretary. (D) Implementation Notwithstanding any other provision of law, the Secretary may implement this paragraph by program instruction or otherwise. (E) Nonapplication of paperwork reduction Act Chapter 35 of title 44, United States Code, shall not apply to the implementation of this paragraph. (4) Definition of affiliate; pharmacy benefit manager In this subsection, the terms affiliate and pharmacy benefit manager have the meaning given those terms in section 1860D\u201312(h)(7). .\n**(3) Enforcement**\n**(A) In general**\nSection 1860D\u20134(b)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(1) ) is amended by adding at the end the following new subparagraph:\n(F) Enforcement of standards for reasonable and relevant contract terms and conditions (i) Allegation submission process (I) In general Not later than January 1, 2028, the Secretary shall establish a process through which a pharmacy may submit to the Secretary an allegation of a violation by a PDP sponsor offering a prescription drug plan of the standards for reasonable and relevant contract terms and conditions under subparagraph (A)(ii), or of subclause (VIII) of this clause. (II) Frequency of submission (aa) In general Except as provided in item (bb), the allegation submission process under this clause shall allow pharmacies to submit any allegations of violations described in subclause (I) not more frequently than once per plan year per contract between a pharmacy and a PDP sponsor. (bb) Allegations relating to contract modifications In the case where a contract between a pharmacy and a PDP sponsor is modified following the submission of allegations by a pharmacy with respect to such contract and plan year, the allegation submission process under this clause shall allow such pharmacy to submit an additional allegation related to those modifications with respect to such contract and plan year. (III) Access to relevant documents and materials A PDP sponsor subject to an allegation under this clause\u2014 (aa) shall provide documents or materials, as specified by the Secretary, including contract offers made by such sponsor to such pharmacy or correspondence related to such offers, to the Secretary at a time, and in a form and manner, specified by the Secretary; and (bb) shall not prohibit or otherwise limit the ability of a pharmacy to submit such documents or materials to the Secretary for the purpose of submitting an allegation or providing evidence for such an allegation under this clause. (IV) Standardized template The Secretary shall establish a standardized template for pharmacies to use for the submission of allegations described in subclause (I). Such template shall require that the submission include a certification by the pharmacy that the information included is accurate, complete, and true to the best of the knowledge, information, and belief of such pharmacy. (V) Preventing frivolous allegations In the case where the Secretary determines that a pharmacy has submitted frivolous allegations under this clause on a routine basis, the Secretary may temporarily prohibit such pharmacy from using the allegation submission process under this clause, as determined appropriate by the Secretary. (VI) Exemption from freedom of information Act Allegations submitted under this clause shall be exempt from disclosure under section 552 of title 5, United States Code. (VII) Rule of construction Nothing in this clause shall be construed as limiting the ability of a pharmacy to pursue other legal actions or remedies, consistent with applicable Federal or State law, with respect to a potential violation of a requirement described in this subparagraph. (VIII) Anti-retaliation and anti-coercion Consistent with applicable Federal or State law, a PDP sponsor shall not\u2014 (aa) retaliate against a pharmacy for submitting any allegations under this clause; or (bb) coerce, intimidate, threaten, or interfere with the ability of a pharmacy to submit any such allegations. (ii) Investigation The Secretary shall investigate, as determined appropriate by the Secretary, allegations submitted pursuant to clause (i). (iii) Enforcement (I) In general In the case where the Secretary determines that a PDP sponsor offering a prescription drug plan has violated the standards for reasonable and relevant contract terms and conditions under subparagraph (A)(ii), the Secretary may use authorities under sections 1857(g) and 1860D\u201312(b)(3)(E) to impose civil monetary penalties or other intermediate sanctions. (II) Application of civil monetary penalties The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil monetary penalty under this clause in the same manner as such provisions apply to a penalty or proceeding under section 1128A(a). .\n**(B) Conforming amendment**\nSection 1857(g)(1) of the Social Security Act ( 42 U.S.C. 1395w\u201327(g)(1) ) is amended\u2014\n**(i)**\nin subparagraph (J), by striking or after the semicolon;\n**(ii)**\nby redesignating subparagraph (K) as subparagraph (L);\n**(iii)**\nby inserting after subparagraph (J), the following new subparagraph:\n(K) fails to comply with the standards for reasonable and relevant contract terms and conditions under subparagraph (A)(ii) of section 1860D\u20134(b)(1); or ;\n**(iv)**\nin subparagraph (L), as redesignated by clause (ii), by striking through (J) and inserting through (K) ; and\n**(v)**\nin the flush matter following subparagraph (L), as so redesignated, by striking subparagraphs (A) through (K) and inserting subparagraphs (A) through (L) .\n**(4) Accountability of pharmacy benefit managers for violations of reasonable and relevant contract terms and conditions**\n**(A) In general**\nSection 1860D\u201312(b) of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ) is amended by adding at the end the following new paragraph:\n(9) Accountability of pharmacy benefit managers for violations of reasonable and relevant contract terms and conditions For plan years beginning on or after January 1, 2028, each contract entered into with a PDP sponsor under this part with respect to a prescription drug plan offered by such sponsor shall provide that any pharmacy benefit manager acting on behalf of such sponsor has a written agreement with the PDP sponsor under which the pharmacy benefit manager agrees to reimburse the PDP sponsor for any amounts paid by such sponsor under section 1860D\u20134(b)(1)(F)(iii)(I) to the Secretary as a result of a violation described in such section if such violation is related to a responsibility delegated to the pharmacy benefit manager by such PDP sponsor. .\n**(B) MA\u2013PD plans**\nSection 1857(f)(3) of the Social Security Act ( 42 U.S.C. 1395w\u201327(f)(3) ) is amended by adding at the end the following new subparagraph:\n(F) Accountability of pharmacy benefit managers for violations of reasonable and relevant contract terms For plan years beginning on or after January 1, 2028, section 1860D\u201312(b)(9). .\n**(5) Biennial report on enforcement and oversight of pharmacy access requirements**\nSection 1860D\u201342 of the Social Security Act ( 42 U.S.C. 1395w\u2013152 ), as amended by paragraph (2), is amended by adding at the end the following new subsection:\n(f) Biennial report on enforcement and oversight of pharmacy access requirements (1) In general Not later than 2 years after the date of enactment of this subsection, and at least once every 2 years thereafter, the Secretary shall publish a report on enforcement and oversight actions and activities undertaken by the Secretary with respect to the requirements under section 1860D\u20134(b)(1). (2) Limitation A report under paragraph (1) shall not disclose\u2014 (A) identifiable information about individuals or entities unless such information is otherwise publicly available; or (B) trade secrets with respect to any entities. .\n**(6) Funding**\nIn addition to amounts otherwise available, there is appropriated to the Centers for Medicare & Medicaid Services Program Management Account, out of any money in the Treasury not otherwise appropriated, $188,000,000 for fiscal year 2026, to remain available until expended, to carry out this subsection.\n##### (b) Modernizing and ensuring PBM accountability\n**(1) In general**\n**(A) Prescription drug plans**\nSection 1860D\u201312 of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ) is amended by adding at the end the following new subsection:\n(h) Requirements relating to pharmacy benefit managers For plan years beginning on or after January 1, 2028: (1) Agreements with pharmacy benefit managers Each contract entered into with a PDP sponsor under this part with respect to a prescription drug plan offered by such sponsor shall provide that any pharmacy benefit manager acting on behalf of such sponsor has a written agreement with the PDP sponsor under which the pharmacy benefit manager, and any affiliates of such pharmacy benefit manager, as applicable, agree to meet the following requirements: (A) No income other than bona fide service fees (i) In general The pharmacy benefit manager and any affiliate of such pharmacy benefit manager shall not derive any remuneration with respect to any services provided on behalf of any entity or individual, in connection with the utilization of covered part D drugs, from any such entity or individual other than bona fide service fees, subject to clauses (ii) and (iii). (ii) Incentive payments For the purposes of this subsection, an incentive payment (as determined by the Secretary) paid by a PDP sponsor to a pharmacy benefit manager that is performing services on behalf of such sponsor shall be deemed a bona fide service fee (even if such payment does not otherwise meet the definition of such term under paragraph (7)(B)) if such payment is a flat dollar amount, is consistent with fair market value (as specified by the Secretary), is related to services actually performed by the pharmacy benefit manager or affiliate of such pharmacy benefit manager, on behalf of the PDP sponsor making such payment, in connection with the utilization of covered part D drugs, and meets additional requirements, if any, as determined appropriate by the Secretary. (iii) Clarification on rebates and discounts used to lower costs for covered part d drugs Rebates, discounts, and other price concessions received by a pharmacy benefit manager or an affiliate of a pharmacy benefit manager from manufacturers, even if such price concessions are calculated as a percentage of a drug\u2019s price, shall not be considered a violation of the requirements of clause (i) if they are fully passed through to a PDP sponsor and are compliant with all regulatory and subregulatory requirements related to direct and indirect remuneration for manufacturer rebates under this part, including in cases where a PDP sponsor is acting as a pharmacy benefit manager on behalf of a prescription drug plan offered by such PDP sponsor. (iv) Evaluation of remuneration arrangements Components of subsets of remuneration arrangements (such as fees or other forms of compensation paid to or retained by the pharmacy benefit manager or affiliate of such pharmacy benefit manager), as determined appropriate by the Secretary, between pharmacy benefit managers or affiliates of such pharmacy benefit managers, as applicable, and other entities involved in the dispensing or utilization of covered part D drugs (including PDP sponsors, manufacturers, pharmacies, and other entities as determined appropriate by the Secretary) shall be subject to review by the Secretary, in consultation with the Office of the Inspector General of the Department of Health and Human Services, as determined appropriate by the Secretary. The Secretary, in consultation with the Office of the Inspector General, shall review whether remuneration under such arrangements is consistent with fair market value (as specified by the Secretary) through reviews and assessments of such remuneration, as determined appropriate. (v) Disgorgement The pharmacy benefit manager shall disgorge any remuneration paid to such pharmacy benefit manager or an affiliate of such pharmacy benefit manager in violation of this subparagraph to the PDP sponsor. (vi) Additional requirements The pharmacy benefit manager shall\u2014 (I) enter into a written agreement with any affiliate of such pharmacy benefit manager, under which the affiliate shall identify and disgorge any remuneration described in clause (v) to the pharmacy benefit manager; and (II) attest, subject to any requirements determined appropriate by the Secretary, that the pharmacy benefit manager has entered into a written agreement described in subclause (I) with any relevant affiliate of the pharmacy benefit manager. (B) Transparency regarding guarantees and cost performance evaluations The pharmacy benefit manager shall\u2014 (i) define, interpret, and apply, in a fully transparent and consistent manner for purposes of calculating or otherwise evaluating pharmacy benefit manager performance against pricing guarantees or similar cost performance measurements related to rebates, discounts, price concessions, or net costs, terms such as\u2014 (I) generic drug , in a manner consistent with the definition of the term under section 423.4 of title 42, Code of Federal Regulations, or a successor regulation; (II) brand name drug , in a manner consistent with the definition of the term under section 423.4 of title 42, Code of Federal Regulations, or a successor regulation; (III) specialty drug ; (IV) rebate ; and (V) discount ; (ii) identify any drugs, claims, or price concessions excluded from any pricing guarantee or other cost performance measure in a clear and consistent manner; and (iii) where a pricing guarantee or other cost performance measure is based on a pricing benchmark other than the wholesale acquisition cost (as defined in section 1847A(c)(6)(B)) of a drug, calculate and provide a wholesale acquisition cost-based equivalent to the pricing guarantee or other cost performance measure. (C) Provision of information (i) In general Not later than July 1 of each year, beginning in 2028, the pharmacy benefit manager shall submit to the PDP sponsor, and to the Secretary, a report, in accordance with this subparagraph, and shall make such report available to such sponsor at no cost to such sponsor in a format specified by the Secretary under paragraph (5). Each such report shall include, with respect to such PDP sponsor and each plan offered by such sponsor, the following information with respect to the previous plan year: (I) A list of all drugs covered by the plan that were dispensed including, with respect to each such drug\u2014 (aa) the brand name, generic or non-proprietary name, and National Drug Code; (bb) the number of plan enrollees for whom the drug was dispensed, the total number of prescription claims for the drug (including original prescriptions and refills, counted as separate claims), and the total number of dosage units of the drug dispensed; (cc) the number of prescription claims described in item (bb) by each type of dispensing channel through which the drug was dispensed, including retail, mail order, specialty pharmacy, long term care pharmacy, home infusion pharmacy, or other types of pharmacies or providers; (dd) the average wholesale acquisition cost, listed as cost per day\u2019s supply, cost per dosage unit, and cost per typical course of treatment (as applicable); (ee) the average wholesale price for the drug, listed as price per day\u2019s supply, price per dosage unit, and price per typical course of treatment (as applicable); (ff) the total out-of-pocket spending by plan enrollees on such drug after application of any benefits under the plan, including plan enrollee spending through copayments, coinsurance, and deductibles; (gg) total rebates paid by the manufacturer on the drug as reported under the Detailed DIR Report (or any successor report) submitted by such sponsor to the Centers for Medicare & Medicaid Services; (hh) all other direct or indirect remuneration on the drug as reported under the Detailed DIR Report (or any successor report) submitted by such sponsor to the Centers for Medicare & Medicaid Services; (ii) the average pharmacy reimbursement amount paid by the plan for the drug in the aggregate and disaggregated by dispensing channel identified in item (cc); (jj) the average National Average Drug Acquisition Cost (NADAC); and (kk) total manufacturer-derived revenue, inclusive of bona fide service fees, attributable to the drug and retained by the pharmacy benefit manager and any affiliate of such pharmacy benefit manager. (II) In the case of a pharmacy benefit manager that has an affiliate that is a retail, mail order, or specialty pharmacy, with respect to drugs covered by such plan that were dispensed, the following information: (aa) The percentage of total prescriptions that were dispensed by pharmacies that are an affiliate of the pharmacy benefit manager for each drug. (bb) The interquartile range of the total combined costs paid by the plan and plan enrollees, per dosage unit, per course of treatment, per 30-day supply, and per 90-day supply for each drug dispensed by pharmacies that are not an affiliate of the pharmacy benefit manager and that are included in the pharmacy network of such plan. (cc) The interquartile range of the total combined costs paid by the plan and plan enrollees, per dosage unit, per course of treatment, per 30-day supply, and per 90-day supply for each drug dispensed by pharmacies that are an affiliate of the pharmacy benefit manager and that are included in the pharmacy network of such plan. (dd) The lowest total combined cost paid by the plan and plan enrollees, per dosage unit, per course of treatment, per 30-day supply, and per 90-day supply, for each drug that is available from any pharmacy included in the pharmacy network of such plan. (ee) The difference between the average acquisition cost of the affiliate, such as a pharmacy or other entity that acquires prescription drugs, that initially acquires the drug and the amount reported under subclause (I)(jj) for each drug. (ff) A list inclusive of the brand name, generic or non-proprietary name, and National Drug Code of covered part D drugs subject to an agreement with a covered entity under section 340B of the Public Health Service Act for which the pharmacy benefit manager or an affiliate of the pharmacy benefit manager had a contract or other arrangement with such a covered entity in the service area of such plan. (III) Where a drug approved under section 505(c) of the Federal Food, Drug, and Cosmetic Act (referred to in this subclause as the listed drug ) is covered by the plan, the following information: (aa) A list of currently marketed generic drugs approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act pursuant to an application that references such listed drug that are not covered by the plan, are covered on the same formulary tier or a formulary tier typically associated with higher cost-sharing than the listed drug, or are subject to utilization management that the listed drug is not subject to. (bb) The estimated average beneficiary cost-sharing under the plan for a 30-day supply of the listed drug. (cc) Where a generic drug listed under item (aa) is on a formulary tier typically associated with higher cost-sharing than the listed drug, the estimated average cost-sharing that a beneficiary would have paid for a 30-day supply of each of the generic drugs described in item (aa), had the plan provided coverage for such drugs on the same formulary tier as the listed drug. (dd) A written justification for providing more favorable coverage of the listed drug than the generic drugs described in item (aa). (ee) The number of currently marketed generic drugs approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act pursuant to an application that references such listed drug. (IV) Where a reference product (as defined in section 351(i) of the Public Health Service Act) is covered by the plan, the following information: (aa) A list of currently marketed biosimilar biological products licensed under section 351(k) of the Public Health Service Act pursuant to an application that refers to such reference product that are not covered by the plan, are covered on the same formulary tier or a formulary tier typically associated with higher cost-sharing than the reference product, or are subject to utilization management that the reference product is not subject to. (bb) The estimated average beneficiary cost-sharing under the plan for a 30-day supply of the reference product. (cc) Where a biosimilar biological product listed under item (aa) is on a formulary tier typically associated with higher cost-sharing than the reference product, the estimated average cost-sharing that a beneficiary would have paid for a 30-day supply of each of the biosimilar biological products described in item (aa), had the plan provided coverage for such products on the same formulary tier as the reference product. (dd) A written justification for providing more favorable coverage of the reference product than the biosimilar biological product described in item (aa). (ee) The number of currently marketed biosimilar biological products licensed under section 351(k) of the Public Health Service Act, pursuant to an application that refers to such reference product. (V) Total gross spending on covered part D drugs by the plan, not net of rebates, fees, discounts, or other direct or indirect remuneration. (VI) The total amount retained by the pharmacy benefit manager or an affiliate of such pharmacy benefit manager in revenue related to utilization of covered part D drugs under that plan, inclusive of bona fide service fees. (VII) The total spending on covered part D drugs net of rebates, fees, discounts, or other direct and indirect remuneration by the plan. (VIII) An explanation of any benefit design parameters under such plan that encourage plan enrollees to fill prescriptions at pharmacies that are an affiliate of such pharmacy benefit manager, such as mail and specialty home delivery programs, and retail and mail auto-refill programs. (IX) The following information: (aa) A list of all brokers, consultants, advisors, and auditors that receive compensation from the pharmacy benefit manager or an affiliate of such pharmacy benefit manager for referrals, consulting, auditing, or other services offered to PDP sponsors related to pharmacy benefit management services. (bb) The amount of compensation provided by such pharmacy benefit manager or affiliate to each such broker, consultant, advisor, and auditor. (cc) The methodology for calculating the amount of compensation provided by such pharmacy benefit manager or affiliate, for each such broker, consultant, advisor, and auditor. (X) A list of all affiliates of the pharmacy benefit manager. (XI) A summary document submitted in a standardized template developed by the Secretary that includes such information described in subclauses (I) through (X). (ii) Written explanation of contracts or agreements with drug manufacturers (I) In general The pharmacy benefit manager shall, not later than 30 days after the finalization of any contract or agreement between such pharmacy benefit manager or an affiliate of such pharmacy benefit manager and a drug manufacturer (or subsidiary, agent, or entity affiliated with such drug manufacturer) that makes rebates, discounts, payments, or other financial incentives related to one or more covered part D drugs or other prescription drugs, as applicable, of the manufacturer directly or indirectly contingent upon coverage, formulary placement, or utilization management conditions on any other covered part D drugs or other prescription drugs, as applicable, submit to the PDP sponsor a written explanation of such contract or agreement. (II) Requirements A written explanation under subclause (I) shall\u2014 (aa) include the manufacturer subject to the contract or agreement, all covered part D drugs and other prescription drugs, as applicable, subject to the contract or agreement and the manufacturers of such drugs, and a high-level description of the terms of such contract or agreement and how such terms apply to such drugs; and (bb) be certified by the Chief Executive Officer, Chief Financial Officer, or General Counsel of such pharmacy benefit manager, or affiliate of such pharmacy benefit manager, as applicable, or an individual delegated with the authority to sign on behalf of one of these officers, who reports directly to the officer. (III) Definition of other prescription drugs For purposes of this clause, the term other prescription drugs means prescription drugs covered as supplemental benefits under this part or prescription drugs paid outside of this part. (D) Audit rights (i) In general Not less than once a year, at the request of the PDP sponsor, the pharmacy benefit manager shall allow for an audit of the pharmacy benefit manager to ensure compliance with all terms and conditions under the written agreement described in this paragraph and the accuracy of information reported under subparagraph (C). (ii) Auditor The PDP sponsor shall have the right to select an auditor. The pharmacy benefit manager shall not impose any limitations on the selection of such auditor. (iii) Provision of information The pharmacy benefit manager shall make available to such auditor all records, data, contracts, and other information necessary to confirm the accuracy of information provided under subparagraph (C), subject to reasonable restrictions on how such information must be reported to prevent redisclosure of such information. (iv) Timing The pharmacy benefit manager must provide information under clause (iii) and other information, data, and records relevant to the audit to such auditor within 6 months of the initiation of the audit and respond to requests for additional information from such auditor within 30 days after the request for additional information. (v) Information from affiliates The pharmacy benefit manager shall be responsible for providing to such auditor information required to be reported under subparagraph (C) or under clause (iii) of this subparagraph that is owned or held by an affiliate of such pharmacy benefit manager. (2) Enforcement (A) In general Each PDP sponsor shall\u2014 (i) disgorge to the Secretary any amounts disgorged to the PDP sponsor by a pharmacy benefit manager under paragraph (1)(A)(v); (ii) require, in a written agreement with any pharmacy benefit manager acting on behalf of such sponsor or affiliate of such pharmacy benefit manager, that such pharmacy benefit manager or affiliate reimburse the PDP sponsor for any civil money penalty imposed on the PDP sponsor as a result of the failure of the pharmacy benefit manager or affiliate to meet the requirements of paragraph (1) that are applicable to the pharmacy benefit manager or affiliate under the agreement; and (iii) require, in a written agreement with any such pharmacy benefit manager acting on behalf of such sponsor or affiliate of such pharmacy benefit manager, that such pharmacy benefit manager or affiliate be subject to punitive remedies for breach of contract for failure to comply with the requirements applicable under paragraph (1). (B) Reporting of alleged violations The Secretary shall make available and maintain a mechanism for manufacturers, PDP sponsors, pharmacies, and other entities that have contractual relationships with pharmacy benefit managers or affiliates of such pharmacy benefit managers to report, on a confidential basis, alleged violations of paragraph (1)(A) or subparagraph (C). (C) Anti-retaliation and anti-coercion Consistent with applicable Federal or State law, a PDP sponsor shall not\u2014 (i) retaliate against an individual or entity for reporting an alleged violation under subparagraph (B); or (ii) coerce, intimidate, threaten, or interfere with the ability of an individual or entity to report any such alleged violations. (3) Certification of compliance (A) In general Each PDP sponsor shall furnish to the Secretary (at a time and in a manner specified by the Secretary) an annual certification of compliance with this subsection, as well as such information as the Secretary determines necessary to carry out this subsection. (B) Implementation Notwithstanding any other provision of law, the Secretary may implement this paragraph by program instruction or otherwise. (4) Rule of construction Nothing in this subsection shall be construed as\u2014 (A) prohibiting flat dispensing fees or reimbursement or payment for ingredient costs (including customary, industry-standard discounts directly related to drug acquisition that are retained by pharmacies or wholesalers) to entities that acquire or dispense prescription drugs; or (B) modifying regulatory requirements or sub-regulatory program instruction or guidance related to pharmacy payment, reimbursement, or dispensing fees. (5) Standard formats (A) In general Not later than June 1, 2027, the Secretary shall specify standard, machine-readable formats for pharmacy benefit managers to submit annual reports required under paragraph (1)(C)(i). (B) Implementation Notwithstanding any other provision of law, the Secretary may implement this paragraph by program instruction or otherwise. (6) Confidentiality (A) In general Information disclosed by a pharmacy benefit manager, an affiliate of a pharmacy benefit manager, a PDP sponsor, or a pharmacy under this subsection that is not otherwise publicly available or available for purchase shall not be disclosed by the Secretary or a PDP sponsor receiving the information, except that the Secretary may disclose the information for the following purposes: (i) As the Secretary determines necessary to carry out this part. (ii) To permit the Comptroller General to review the information provided. (iii) To permit the Director of the Congressional Budget Office to review the information provided. (iv) To permit the Executive Director of the Medicare Payment Advisory Commission to review the information provided. (v) To the Attorney General for the purposes of conducting oversight and enforcement under this title. (vi) To the Inspector General of the Department of Health and Human Services in accordance with its authorities under the Inspector General Act of 1978 (section 406 of title 5, United States Code), and other applicable statutes. (B) Restriction on use of information The Secretary, the Comptroller General, the Director of the Congressional Budget Office, and the Executive Director of the Medicare Payment Advisory Commission shall not report on or disclose information disclosed pursuant to subparagraph (A) to the public in a manner that would identify\u2014 (i) a specific pharmacy benefit manager, affiliate, pharmacy, manufacturer, wholesaler, PDP sponsor, or plan; or (ii) contract prices, rebates, discounts, or other remuneration for specific drugs in a manner that may allow the identification of specific contracting parties or of such specific drugs. (7) Definitions For purposes of this subsection: (A) Affiliate The term affiliate means, with respect to any pharmacy benefit manager or PDP sponsor, any entity that, directly or indirectly\u2014 (i) owns or is owned by, controls or is controlled by, or is otherwise related in any ownership structure to such pharmacy benefit manager or PDP sponsor; or (ii) acts as a contractor, principal, or agent to such pharmacy benefit manager or PDP sponsor, insofar as such contractor, principal, or agent performs any of the functions described under subparagraph (C). (B) Bona fide service fee The term bona fide service fee means a fee that is reflective of the fair market value (as specified by the Secretary, through notice and comment rulemaking) for a bona fide, itemized service actually performed on behalf of an entity, that the entity would otherwise perform (or contract for) in the absence of the service arrangement and that is not passed on in whole or in part to a client or customer, whether or not the entity takes title to the drug. Such fee must be a flat dollar amount and shall not be directly or indirectly based on, or contingent upon\u2014 (i) drug price, such as wholesale acquisition cost or drug benchmark price (such as average wholesale price); (ii) the amount of discounts, rebates, fees, or other direct or indirect remuneration with respect to covered part D drugs dispensed to enrollees in a prescription drug plan, except as permitted pursuant to paragraph (1)(A)(ii); (iii) coverage or formulary placement decisions or the volume or value of any referrals or business generated between the parties to the arrangement; or (iv) any other amounts or methodologies prohibited by the Secretary. (C) Pharmacy benefit manager The term pharmacy benefit manager means any person or entity that, either directly or through an intermediary, acts as a price negotiator or group purchaser on behalf of a PDP sponsor or prescription drug plan, or manages the prescription drug benefits provided by such sponsor or plan, including the processing and payment of claims for prescription drugs, the performance of drug utilization review, the processing of drug prior authorization requests, the adjudication of appeals or grievances related to the prescription drug benefit, contracting with network pharmacies, controlling the cost of covered part D drugs, or the provision of related services. Such term includes any person or entity that carries out one or more of the activities described in the preceding sentence, irrespective of whether such person or entity calls itself a pharmacy benefit manager . .\n**(B) MA\u2013PD plans**\nSection 1857(f)(3) of the Social Security Act ( 42 U.S.C. 1395w\u201327(f)(3) ), as amended by subsection (a)(4)(B), is amended by adding at the end the following new subparagraph:\n(G) Requirements relating to pharmacy benefit managers For plan years beginning on or after January 1, 2028, section 1860D\u201312(h). .\n**(C) Nonapplication of paperwork reduction Act**\nChapter 35 of title 44, United States Code, shall not apply to the implementation of this paragraph.\n**(D) Funding**\n**(i) Secretary**\nIn addition to amounts otherwise available, there is appropriated to the Centers for Medicare & Medicaid Services Program Management Account, out of any money in the Treasury not otherwise appropriated, $113,000,000 for fiscal year 2026, to remain available until expended, to carry out this paragraph.\n**(ii) OIG**\nIn addition to amounts otherwise available, there is appropriated to the Inspector General of the Department of Health and Human Services, out of any money in the Treasury not otherwise appropriated, $20,000,000 for fiscal year 2026, to remain available until expended, to carry out this paragraph.\n**(2) GAO study and report on price-related compensation across the supply chain**\n**(A) Study**\nThe Comptroller General of the United States (in this paragraph referred to as the Comptroller General ) shall conduct a study describing the use of compensation and payment structures related to a prescription drug\u2019s price within the retail prescription drug supply chain in part D of title XVIII of the Social Security Act ( 42 U.S.C. 1395w\u2013101 et seq. ). Such study shall summarize information from Federal agencies and industry experts, to the extent available, with respect to the following:\n**(i)**\nThe type, magnitude, other features (such as the pricing benchmarks used), and prevalence of compensation and payment structures related to a prescription drug\u2019s price, such as calculating fee amounts as a percentage of a prescription drug\u2019s price, between intermediaries in the prescription drug supply chain, including\u2014\n**(I)**\npharmacy benefit managers;\n**(II)**\nPDP sponsors offering prescription drug plans and Medicare Advantage organizations offering MA\u2013PD plans;\n**(III)**\ndrug wholesalers;\n**(IV)**\npharmacies;\n**(V)**\nmanufacturers;\n**(VI)**\npharmacy services administrative organizations;\n**(VII)**\nbrokers, auditors, consultants, and other entities that\u2014\n**(aa)**\nadvise PDP sponsors offering prescription drug plans and Medicare Advantage organizations offering MA\u2013PD plans regarding pharmacy benefits; or\n**(bb)**\nreview PDP sponsor and Medicare Advantage organization contracts with pharmacy benefit managers; and\n**(VIII)**\nother service providers that contract with any of the entities described in subclauses (I) through (VII) that may use price-related compensation and payment structures, such as rebate aggregators (or other entities that negotiate or process price concessions on behalf of pharmacy benefit managers, plan sponsors, or pharmacies).\n**(ii)**\nThe primary business models and compensation structures for each category of intermediary described in clause (i).\n**(iii)**\nVariation in price-related compensation structures between affiliated entities (such as entities with common ownership, either full or partial, and subsidiary relationships) and unaffiliated entities.\n**(iv)**\nPotential conflicts of interest among contracting entities related to the use of prescription drug price-related compensation structures, such as the potential for fees or other payments set as a percentage of a prescription drug\u2019s price to advantage formulary selection, distribution, or purchasing of prescription drugs with higher prices.\n**(v)**\nNotable differences, if any, in the use and level of price-based compensation structures over time and between different market segments, such as under part D of title XVIII of the Social Security Act ( 42 U.S.C. 1395w\u2013101 et seq. ) and the Medicaid program under title XIX of such Act ( 42 U.S.C. 1396 et seq. ).\n**(vi)**\nThe effects of drug price-related compensation structures and alternative compensation structures on Federal health care programs and program beneficiaries, including with respect to cost-sharing, premiums, Federal outlays, biosimilar and generic drug adoption and utilization, drug shortage risks, and the potential for fees set as a percentage of a drug\u2019s price to advantage the formulary selection, distribution, or purchasing of drugs with higher prices.\n**(vii)**\nOther issues determined to be relevant and appropriate by the Comptroller General.\n**(B) Report**\nNot later than 2 years after the date of enactment of this paragraph, the Comptroller General shall submit to Congress a report containing the results of the study conducted under subparagraph (A), together with recommendations for such legislation and administrative action as the Comptroller General determines appropriate.\n**(3) MedPAC reports on agreements with pharmacy benefit managers with respect to prescription drug plans and ma-pd plans**\n**(A) In general**\nThe Medicare Payment Advisory Commission shall submit to Congress the following reports:\n**(i) Initial report**\nNot later than the first March 15 occurring after the date that is 2 years after the date on which the Secretary makes the data available to the Commission, a report regarding agreements with pharmacy benefit managers with respect to prescription drug plans and MA\u2013PD plans. Such report shall include, to the extent practicable\u2014\n**(I)**\na description of trends and patterns, including relevant averages, totals, and other figures for the types of information submitted;\n**(II)**\nan analysis of any differences in agreements and their effects on plan enrollee out-of-pocket spending and average pharmacy reimbursement, and other impacts; and\n**(III)**\nany recommendations the Commission determines appropriate.\n**(ii) Final report**\nNot later than 2 years after the date on which the Commission submits the initial report under clause (i), a report describing any changes with respect to the information described in clause (i) over time, together with any recommendations the Commission determines appropriate.\n**(B) Funding**\nIn addition to amounts otherwise available, there is appropriated to the Medicare Payment Advisory Commission, out of any money in the Treasury not otherwise appropriated, $1,000,000 for fiscal year 2026, to remain available until expended, to carry out this paragraph.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4317",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PBM Reform Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-07T14:02:13Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3345is.xml"
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
      "title": "PBM Price Transparency and Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PBM Price Transparency and Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XVIII and XIX of the Social Security Act to ensure accurate payments to pharmacies under Medicaid and prevent the use of abusive spread pricing in Medicaid, and to assure pharmacy access and choice for Medicare beneficiaries and modernize and ensure PBM accountability under Medicare.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:15Z"
    }
  ]
}
```
