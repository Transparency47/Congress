# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2534
- Title: Veteran Families Health Services Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2534
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2025-12-10T06:54:56Z
- Update date including text: 2025-12-10T06:54:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2534",
    "number": "2534",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Veteran Families Health Services Act of 2025",
    "type": "S",
    "updateDate": "2025-12-10T06:54:56Z",
    "updateDateIncludingText": "2025-12-10T06:54:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T15:14:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NJ"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NV"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-30",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NH"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CO"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "RI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-30",
      "state": "ME"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "VT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NM"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "AZ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NV"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "VA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "WI"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2534is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2534\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mrs. Murray (for herself, Ms. Duckworth , Mr. Booker , Mr. Schumer , Mr. Blumenthal , Mr. Merkley , Ms. Rosen , Ms. Warren , Mr. Sanders , Ms. Klobuchar , Mrs. Shaheen , Mr. Hickenlooper , Mr. Whitehouse , Mr. King , Ms. Smith , Mr. Welch , Mr. Heinrich , Mrs. Gillibrand , Mr. Wyden , Mr. Padilla , Mr. Gallego , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo improve the reproductive assistance provided by the Department of Defense and the Department of Veterans Affairs to certain members of the Armed Forces, veterans, and their spouses or partners, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Veteran Families Health Services Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Reproductive and fertility preservation assistance for members of the Armed Forces\nSec. 101. Definitions.\nSec. 102. Provision of fertility treatment and counseling to members of the Armed Forces and spouses, partners, and gestational surrogates of such members.\nSec. 103. Establishment of fertility preservation procedures after an injury or illness.\nSec. 104. Cryopreservation and storage of reproductive genetic material of members of the Armed Forces on active duty.\nSec. 105. Assistance with and continuity of care regarding reproductive and fertility preservation services.\nSec. 106. Coordination between Department of Defense and Department of Veterans Affairs on furnishing of fertility treatment and counseling.\nSec. 107. Regulations.\nTITLE II\u2014Reproductive and adoption assistance for veterans\nSec. 201. Inclusion of fertility treatment and counseling under definition of medical services.\nSec. 202. Fertility treatment and counseling for certain veterans and spouses, partners, and gestational surrogates of such veterans.\nSec. 203. Adoption assistance for certain veterans.\nSec. 204. Assistance with and continuity of care regarding reproductive and fertility preservation services.\nSec. 205. Facilitation of reproduction and infertility research.\nSec. 206. Regulations on furnishing of fertility treatment and counseling and adoption assistance by Department of Veterans Affairs.\nI\nReproductive and fertility preservation assistance for members of the Armed Forces\n#### 101. Definitions\nIn this title:\n**(1) Active duty**\nThe term active duty has the meaning given that term in section 101(d)(1) of title 10, United States Code.\n**(2) Armed forces**\nThe term Armed Forces has the meaning given the term armed forces in section 101(a)(4) of such title.\n#### 102. Provision of fertility treatment and counseling to members of the Armed Forces and spouses, partners, and gestational surrogates of such members\n##### (a) Fertility treatment and counseling\n**(1) In general**\nThe Secretary of Defense shall make available fertility treatment and counseling to a member of the Armed Forces or a spouse, partner, or gestational surrogate of such a member.\n**(2) Eligibility for treatment and counseling**\nFertility treatment and counseling shall be furnished under paragraph (1) without regard to the sex, sex characteristics, gender identity, sexual orientation, infertility diagnosis, or marital status of the member of the Armed Forces or their spouse or partner.\n**(3) In vitro fertilization**\nIn the case of in vitro fertilization treatment furnished under paragraph (1), the Secretary may furnish to an individual under such paragraph\u2014\n**(A)**\nnot more than three completed oocyte retrievals; and\n**(B)**\nunlimited embryo transfers.\n##### (b) Procurement of reproductive genetic material\nIf a member of the Armed Forces is unable to provide their reproductive genetic material, such as oocytes, sperm, or embryos, for purposes of fertility treatment under subsection (a), the Secretary shall, at the election of such member, allow such member to receive such treatment with donated reproductive genetic material and pay or reimburse such member the reasonable costs of procuring such material from a donor.\n##### (c) Rules of construction\n**(1) Impact on existing authority**\nNothing in this section shall be construed to rescind the authority of the Secretary to provide in vitro fertilization benefits pursuant to section 1074(c)(4) of title 10, United States Code.\n**(2) Sourcing of gestational surrogate or reproductive genetic material**\nNothing in this section shall be construed to require the Secretary\u2014\n**(A)**\nto find or certify a gestational surrogate for a member of the Armed Forces or to connect a gestational surrogate with such a member; or\n**(B)**\nto find or certify reproductive genetic material, such as oocytes, sperm, or embryos, from a donor for a member of the Armed Forces or to connect such a member with reproductive genetic material from a donor.\n##### (d) Definitions\nIn this section:\n**(1) Fertility treatment**\nThe term fertility treatment includes the following:\n**(A)**\nPreservation of human oocytes, sperm, or embryos.\n**(B)**\nArtificial insemination, including intravaginal insemination, intracervical insemination, and intrauterine insemination.\n**(C)**\nAssisted reproductive technology, including in vitro fertilization and other treatments or procedures in which reproductive genetic material, such as oocytes, sperm, or embryos, are handled, when clinically appropriate.\n**(D)**\nGenetic testing of embryos.\n**(E)**\nMedications prescribed or obtained over-the-counter, as indicated for fertility.\n**(F)**\nGamete donation.\n**(G)**\nSuch other information, referrals, treatments, procedures, medications, laboratory testing, technologies, and services relating to fertility as the Secretary of Defense determines appropriate.\n**(2) Gestational surrogate**\nThe term gestational surrogate means an adult, who is not the intended parent, who enters into a surrogacy agreement to become pregnant through in vitro fertilization using gametes that are not the gametes of that individual.\n**(3) Partner**\nThe term partner , with respect to a member of the Armed Forces, means an individual selected by the member who agrees to be a parent, with the member, of a child born as a result of the use of any fertility treatment under this section.\n#### 103. Establishment of fertility preservation procedures after an injury or illness\n##### (a) In general\nThe Secretary of Defense, acting through the Assistant Secretary of Defense for Health Affairs, shall establish procedures for the retrieval of reproductive genetic material, such as sperm or oocytes, as soon as medically appropriate, from a member of the Armed Forces in cases in which the fertility of such member is potentially jeopardized as a result of an injury or illness incurred or aggravated while serving on active duty in the Armed Forces in order to preserve the medical options of such member.\n##### (b) Inclusion of information in advanced directives and military testamentary instruments\nThe Secretary of Defense shall ensure that any advance medical directive, as defined in section 1044c(b) of title 10, United States Code, or military testamentary instrument, as defined in section 1044d(b) of such title, completed by a member of the Armed Forces includes questions about the consent of the member to fertility preservation procedures under subsection (a) and about rights, ownership, and use of reproductive genetic material.\n#### 104. Cryopreservation and storage of reproductive genetic material of members of the Armed Forces on active duty\n##### (a) In general\nThe Secretary of Defense shall provide members of the Armed Forces on active duty with the opportunity for retrieval, testing, cryopreservation, shipping, and storage of their reproductive genetic material, such as sperm or oocytes, prior to\u2014\n**(1)**\ndeployment to a combat zone; or\n**(2)**\na duty assignment that includes a hazardous assignment, including\u2014\n**(A)**\nassignments resulting in exposure to perfluoroalkyl or polyfluoroalkyl substances; and\n**(B)**\nsuch other assignments as determined by the Secretary.\n##### (b) Period of time\n**(1) In general**\nThe Secretary shall provide for the retrieval, testing, cryopreservation, shipping, and storage of reproductive genetic material of any member of the Armed Forces under subsection (a), at no cost to the member, until the date that is one year after the retirement, separation, or release of the member from the Armed Forces.\n**(2) Continued cryopreservation and storage**\nAt the end of the one-year period specified in paragraph (1), the Secretary shall permit an individual whose reproductive genetic material was cryopreserved and stored as described in that paragraph to select, including pursuant to an advance medical directive or military testamentary instrument completed under subsection (c), one of the following options:\n**(A)**\nTo continue such cryopreservation and storage in such facility with the cost of such cryopreservation and storage borne by the individual.\n**(B)**\nTo transfer the material to a private cryopreservation and storage facility selected by the individual.\n##### (c) Advance medical directive and military testamentary instrument\nA member of the Armed Forces who elects to cryopreserve and store their reproductive genetic material under this section must complete an advance medical directive, as defined in section 1044c(b) of title 10, United States Code, and a military testamentary instrument, as defined in section 1044d(b) of such title, that explicitly specifies the use of their cryopreserved and stored reproductive genetic material if such member dies or otherwise loses the capacity to consent to the use of their cryopreserved and stored reproductive genetic material.\n#### 105. Assistance with and continuity of care regarding reproductive and fertility preservation services\nThe Secretary of Defense shall ensure that employees of the Department of Defense assist members of the Armed Forces\u2014\n**(1)**\nin navigating the services provided under this title;\n**(2)**\nin finding a provider that meets the needs of such members with respect to such services; and\n**(3)**\nin continuing the receipt of such services without interruption during a permanent change of station for such members.\n#### 106. Coordination between Department of Defense and Department of Veterans Affairs on furnishing of fertility treatment and counseling\n##### (a) In general\nThe Secretary of Defense and the Secretary of Veterans Affairs shall share best practices and facilitate referrals, as they consider appropriate, on the furnishing of fertility treatment and counseling to individuals eligible for the receipt of such counseling and treatment from each such Secretary.\n##### (b) Memorandum of understanding\nThe Secretary of Defense and the Secretary of Veterans Affairs shall enter into a memorandum of understanding\u2014\n**(1)**\nregarding coordination of fertility preservation care and continuation of coverage, without interruption, for a member of the Armed Forces who is transitioning to veteran status; and\n**(2)**\nauthorizing the Department of Veterans Affairs to compensate the Department of Defense for the cryopreservation, transportation, and storage of reproductive genetic material of veterans under section 104(b)(2)(A).\n#### 107. Regulations\nNot later than two years after the date of the enactment of this Act, the Secretary of Defense shall prescribe regulations to carry out this title.\nII\nReproductive and adoption assistance for veterans\n#### 201. Inclusion of fertility treatment and counseling under definition of medical services\nSection 1701(6) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(J) Fertility treatment and counseling under section 1720M of this title. .\n#### 202. Fertility treatment and counseling for certain veterans and spouses, partners, and gestational surrogates of such veterans\n##### (a) In general\nSubchapter II of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1720M. Fertility treatment and counseling for certain veterans and spouses, partners, and gestational surrogates of such veterans (a) Requirement (1) In general Notwithstanding any other provision of law, including the surrogacy laws of any State, the Secretary shall furnish fertility treatment and counseling for the benefit of a covered veteran to the veteran and the spouse, partner, gamete donor, or gestational surrogate of the veteran if the veteran, and the spouse, partner, gamete donor, or gestational surrogate of the veteran, as applicable, each provide informed consent for such treatment and counseling, including for each cycle of treatment authorized under this section, through a process prescribed by the Secretary. (2) Provision of treatment and counseling Fertility treatment and counseling shall be furnished under paragraph (1) without regard to the sex, sexual characteristics, gender identity, sexual orientation, infertility diagnosis, or marital status of the covered veteran or their spouse or partner. (3) In vitro fertilization In the case of in vitro fertilization treatment furnished under paragraph (1), the Secretary may furnish to an individual under such paragraph\u2014 (A) not more than three completed oocyte retrievals; and (B) unlimited embryo transfers. (4) Copayment The Secretary shall only furnish fertility treatment and counseling under paragraph (1) to a covered veteran who is required to pay to the United States a copayment amount as a condition for the receipt of hospital care, medical services, or medications under this chapter if the covered veteran agrees to pay such applicable copayment amount to the United States for such treatment and counseling. (b) Procurement of reproductive genetic material (1) In general If a covered veteran is unable to provide their reproductive genetic material for purposes of fertility treatment under subsection (a), the Secretary shall, at the election of such veteran\u2014 (A) allow such veteran to receive such treatment with donated reproductive genetic material, if the donor provides informed consent for use of such material; and (B) pay or reimburse the veteran, donor, or a party acting on behalf of the donor the reasonable costs of procuring such material from the donor. (2) Other expenses The Secretary may pay or reimburse a covered veteran a reasonable amount for personal travel and incidental expenses associated with procuring material from a donor under paragraph (1). (c) Outreach and training The Secretary shall carry out an outreach and training program to ensure veterans and health care providers of the Department are aware of\u2014 (1) the availability of and eligibility requirements for fertility treatment and counseling under this section; and (2) any changes to fertility treatment and counseling covered under this section. (d) Ownership, use, or disposition of reproductive genetic material (1) In general Issues or disputes regarding ownership of reproductive genetic material or future use or disposition of such material shall be the sole responsibility of the covered veteran and the spouse, partner, or gestational surrogate of the veteran, as applicable, and the private facility storing such material. (2) Role of Department The role of the Secretary under this section is limited to furnishing the treatment and counseling required under this section when requested by a covered veteran and determined necessary by the Secretary. (3) Ownership and custody of reproductive genetic material The Secretary will not have ownership or custody of any reproductive genetic material obtained pursuant to treatment under this section and will not be involved in the ultimate disposition of such material or disputes between or among any parties with respect to such material. (e) Rule of construction Nothing in this section shall be construed to require the Secretary\u2014 (1) to find or certify a gestational surrogate for a covered veteran or to connect a gestational surrogate with a covered veteran; or (2) to furnish maternity care to a covered veteran or spouse, partner, or gestational surrogate of a covered veteran beyond what is otherwise required or authorized by law. (f) Definitions In this section: (1) The term covered veteran means a veteran who is enrolled in the system of annual patient enrollment established under section 1705(a) of this title. (2) The term fertility treatment includes the following: (A) Preservation of human oocytes, sperm, or embryos. (B) Artificial insemination, including intravaginal insemination, intracervical insemination, and intrauterine insemination. (C) Assisted reproductive technology, including in vitro fertilization and other treatments or procedures in which reproductive genetic material, such as oocytes, sperm, or embryos, are handled, when clinically appropriate. (D) Genetic testing of embryos. (E) Medications prescribed or obtained over-the-counter, as indicated for fertility. (F) Gamete donation. (G) Such other information, referrals, treatments, procedures, medications, laboratory testing, technologies, and services relating to fertility as the Secretary determines appropriate. (3) The term gestational surrogate means an adult, who is not the intended parent, who enters into a surrogacy agreement to become pregnant through in vitro fertilization using gametes that are not the gametes of that individual. (4) The term partner , with respect to a covered veteran, means an individual selected by the veteran who agrees to be a parent, with the veteran, of a child born as a result of the use of any fertility treatment under this section. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 17 of such title is amended by inserting after the item relating to section 1720L the following new item:\n1720M. Fertility treatment and counseling for certain veterans and spouses, partners, and gestational surrogates of such veterans. .\n##### (c) Sunset of existing authority\nThe authority under section 234 of the Military Construction, Veterans Affairs, and Related Agencies Appropriations Act, 2024 (division A of Public Law 118\u201342 ), or any similar authority subsequently enacted by law, shall cease on the effective date of regulations prescribed to carry out section 1720M of title 38, United States Code, as added by subsection (a).\n#### 203. Adoption assistance for certain veterans\n##### (a) In general\nSubchapter VIII of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1790. Adoption assistance (a) In general The Secretary may pay an amount, not to exceed the limitation amount, to assist a covered veteran in the adoption of one or more children, without regard to the sex, gender identity, sexual orientation, or marital status of the covered veteran. (b) Limitation amount For purposes of this section, the limitation amount is the amount equal to the cost the Department would incur by paying the expenses of not more than three adoptions by covered veterans, as determined by the Secretary. (c) Covered veteran defined In this section, the term covered veteran has the meaning given that term in section 1720M(f) of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 17 of such title is amended by inserting after the item relating to section 1789 the following new item:\n1790. Adoption assistance. .\n#### 204. Assistance with and continuity of care regarding reproductive and fertility preservation services\nThe Secretary of Veterans Affairs shall ensure that employees of the Department of Veterans Affairs assist veterans\u2014\n**(1)**\nin navigating the services provided under this title and the amendments made by this title;\n**(2)**\nin finding a provider that meets the needs of such veterans with respect to such services; and\n**(3)**\nin continuing the receipt of such services without interruption if such veterans move to a different geographic location.\n#### 205. Facilitation of reproduction and infertility research\n##### (a) In general\nSubchapter II of chapter 73 of title 38, United States Code, is amended by adding at the end the following new section:\n7330E. Facilitation of reproduction and infertility research (a) Facilitation of research required The Secretary shall facilitate research conducted collaboratively by the Secretary of Defense and the Secretary of Health and Human Services to improve the ability of the Department of Veterans Affairs to meet the long-term reproductive health care needs of veterans who have a condition that affects the ability of the individual to reproduce. (b) Dissemination of information The Secretary shall ensure that information produced by the research facilitated under this section that may be useful for other activities of the Veterans Health Administration is disseminated throughout the Veterans Health Administration. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 73 of such title is amended by inserting after the item relating to section 7330D the following new item:\n7330E. Facilitation of reproduction and infertility research. .\n#### 206. Regulations on furnishing of fertility treatment and counseling and adoption assistance by Department of Veterans Affairs\nNot later than two years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall prescribe regulations\u2014\n**(1)**\nto carry out section 1720M of title 38, United States Code, as added by section 202(a); and\n**(2)**\nto carry out section 1790 of such title, as added by section 203(a).",
      "versionDate": "2025-07-30",
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
        "actionDate": "2025-08-01",
        "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4855",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veteran Families Health Services Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:57:14Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2534is.xml"
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
      "title": "Veteran Families Health Services Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veteran Families Health Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the reproductive assistance provided by the Department of Defense and the Department of Veterans Affairs to certain members of the Armed Forces, veterans, and their spouses or partners, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T04:48:20Z"
    }
  ]
}
```
