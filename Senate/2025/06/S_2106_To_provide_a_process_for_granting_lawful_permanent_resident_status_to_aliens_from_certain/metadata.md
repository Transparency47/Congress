# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2106
- Title: SECURE Act
- Congress: 119
- Bill type: S
- Bill number: 2106
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-02-27T12:03:21Z
- Update date including text: 2026-02-27T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2106",
    "number": "2106",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "SECURE Act",
    "type": "S",
    "updateDate": "2026-02-27T12:03:21Z",
    "updateDateIncludingText": "2026-02-27T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
            "date": "2025-06-18T16:41:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-18T16:41:15Z",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-18",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "NY"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2106is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2106\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Van Hollen (for himself, Ms. Alsobrooks , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Mr. Booker , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kim , Ms. Klobuchar , Mr. Markey , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Ms. Smith , Mr. Warner , Mr. Warnock , Ms. Warren , Mr. Whitehouse , Mr. Wyden , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide a process for granting lawful permanent resident status to aliens from certain countries who meet certain eligibility requirements, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Safe Environment from Countries Under Repression and Emergency Act or the SECURE Act .\n#### 2. Adjustment of status of certain foreign nationals\n##### (a) In general\nChapter 5 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1255 et seq. ) is amended by inserting after section 245A ( 8 U.S.C. 1255A ) the following:\n245B. Adjustment of status of certain foreign nationals (a) In general (1) Authorization (A) In general Notwithstanding section 245(c), the status of any alien described in subsection (b)(1) shall be adjusted by the Secretary of Homeland Security to that of an alien lawfully admitted for permanent residence if the alien\u2014 (i) is not inadmissible under paragraph (2) or (3) of section 212(a); (ii) is not deportable under paragraph (2), (3), or (4) of section 237(a); and (iii) is not described in section 208(b)(2)(A)(i). (B) Treatment of expunged convictions In this section, the term conviction does not include a judgment that has been expunged or set aside that resulted in a rehabilitative disposition or the equivalent. (2) Application (A) In general Except as provided in subparagraph (B), any alien who is physically present in the United States may apply for adjustment of status under this section. (B) Applications from outside the united states for certain aliens previously removed or who departed In the case of an alien who, on or after September 28, 2016, was removed from the United States or departed pursuant to an order of voluntary departure, the alien may apply for adjustment of status under this section from outside the United States if, on the day before the date on which the alien was so removed or so departed, the alien was an alien described in subsection (b)(1). (C) Fee (i) In general The Secretary of Homeland Security shall require any alien applying for permanent resident status under this section to pay a reasonable fee that is commensurate with the cost of processing the application. Such fee may not exceed $1,440. (ii) Fee exemption An applicant may be exempted from paying the application fee required under clause (i) if the applicant\u2014 (I) is younger than 18 years of age; (II) received total income, during the 12-month period immediately preceding the date on which the applicant files an application under this section, that is less than 150 percent of the Federal poverty line; (III) is in foster care or otherwise lacking any parental or other familial support; or (IV) cannot care for himself or herself because of a serious, chronic disability. (D) Relationship of application to certain orders (i) Motion not required An alien described in subparagraph (A) or (B) who has been the subject of an order of removal or voluntary departure may not be required, as a condition of submitting or approving an application under such subparagraph, to file a motion to reopen, reconsider, or vacate such order. (ii) Approval If the Secretary of Homeland Security approves an application submitted by an alien under this paragraph, the Secretary shall cancel any order of removal or voluntary departure to which the alien is or was subject. (iii) Denial If the Secretary of Homeland Security renders a final administrative decision to deny an application submitted by an alien under this paragraph, any order of removal or voluntary departure to which the alien is subject shall be effective and enforceable to the same extent as if such application had not been made. (b) Aliens eligible for adjustment of status (1) In general An alien is described in this subsection if the alien\u2014 (A) is a national of a foreign state that was at any time designated under section 244(b); (B) (i) is in temporary protected status under section 244; (ii) held temporary protected status as a national of a designated foreign state described in subparagraph (A); (iii) qualified for temporary protected status on the date on which the last designation or extension was made by the Secretary of Homeland Security; or (iv) was present in the United States pursuant to a grant of deferred enforced departure that had been extended beyond or was issued after September 28, 2016; (C) (i) has been continuously present in the United States for not less than 3 years and is physically present in the United States on the date on which the alien files an application for adjustment of status under this section; or (ii) in the case of an alien who, on or after September 28, 2016, was removed from the United States or departed pursuant to an order of voluntary departure, was continuously present in the United States for a period of not less than 3 years before the date on which the alien was so removed or so departed; and (D) passes all applicable criminal and national security background checks. (2) Short absences An alien shall not be considered to have failed to maintain continuous physical presence in the United States under paragraph (1)(C) by reason of an absence, or multiple absences, from the United States for any period or periods that do not exceed, in the aggregate, 180 days. (3) Waiver authorized Notwithstanding any provision of this Act, an alien who fails to meet the continuous physical presence requirement under paragraph (1)(C) shall be considered eligible for adjustment of status under this section if the Attorney General or the Secretary of Homeland Security, as applicable, determines that the removal or continued absence of the alien from the United States, as applicable, would result in extreme hardship to the alien or to the alien\u2019s spouse, children, parents, or domestic partner. (c) Stay of removal (1) In general Except as provided in paragraph (2), an alien who is subject to a final order of removal may not be removed if the alien\u2014 (A) has a pending application under subsection (a); or (B) (i) is prima facie eligible to file an application under subsection (a); and (ii) indicates that he or she intends to file such an application. (2) Exception Paragraph (1) shall not apply to any alien whose application under subsection (a) has been denied by the Secretary of Homeland Security in a final administrative determination. (3) During certain proceedings (A) In general Except as provided in subparagraph (B) and notwithstanding any other provision of this Act, the Secretary of Homeland Security may not order any alien to be removed from the United States if the alien raises, as a defense to such an order, the eligibility of the alien to apply for adjustment of status under subsection (a). (B) Exception Subparagraph (A) shall not apply to any alien whose application under subsection (a) has been denied by the Secretary of Homeland Security in a final administrative determination. (4) Work authorization The Secretary of Homeland Security\u2014 (A) shall authorize any alien who has applied for adjustment of status under subsection (a) to engage in employment in the United States while such application is pending; and (B) may provide such alien with an employment authorized endorsement or other appropriate document signifying such employment authorization. (d) Advance parole (1) In general During the period beginning on the date on which an alien applies for adjustment of status under this Act and ending on the date on which the Secretary of Homeland Security makes a final decision regarding such application, the alien shall be eligible to apply for advance parole. (2) Applicability Section 101(g) shall not apply to an alien granted advance parole under this subsection. (e) Adjustment of status for spouses and children (1) In general Notwithstanding section 245(c) and except as provided in paragraphs (2) and (3), the Secretary of Homeland Security shall adjust the status of an alien to that of an alien lawfully admitted for permanent residence if the alien\u2014 (A) is the spouse, domestic partner, child, or unmarried son or daughter of an alien whose status has been adjusted to that of an alien lawfully admitted for permanent residence under subsection (a); (B) is physically present in the United States on the date on which the alien files an application for such adjustment of status; and (C) is otherwise eligible to receive an immigrant visa and is otherwise admissible to the United States for permanent residence. (2) Continuous presence requirement (A) In general The status of an unmarried son or daughter referred to in paragraph (1)(A) may not be adjusted under paragraph (1) until such son or daughter establishes that he or she has been physically present in the United States for at least 1 year. (B) Short absences An alien shall not be considered to have failed to maintain continuous physical presence in the United States under subparagraph (A) by reason of an absence, or multiple absences, from the United States for any period or periods that do not exceed, in the aggregate, 180 days. (3) Waiver In determining eligibility and admissibility under paragraph (1)(C), the grounds for inadmissibility under paragraphs (4), (5), (6), (7)(A), and (9) of section 212(a) shall not apply. (f) Availability of administrative review The Secretary of Homeland Security shall provide applicants for adjustment of status under subsection (a) the same right to, and procedures for, administrative review as are provided to\u2014 (1) applicants for adjustment of status under section 245; or (2) aliens who are subject to removal proceedings under section 240. (g) Exceptions to numerical limitations The numerical limitations set forth in sections 201 and 202 shall not apply to aliens whose status is adjusted pursuant to subsection (a). .\n##### (b) Clarification of inspection and admission under Temporary Protected Status\nSection 244(f)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(f)(4) ) is amended by inserting as having been inspected and admitted into the United States, and after considered .\n##### (c) Clerical amendment\nThe table of contents for the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended by inserting after the item relating to section 245A the following:\nSec. 245B. Adjustment of status of certain foreign nationals. .\n#### 3. Confidentiality of information\n##### (a) In general\nThe Secretary of Homeland Security may not disclose or use information provided in applications filed under section 245B of the Immigration and Nationality Act, as added by section 2, for the purpose of immigration enforcement.\n##### (b) Referrals prohibited\nThe Secretary may not refer any individual who has been granted permanent resident status under section 245B of the Immigration and Nationality Act to U.S. Immigration and Customs Enforcement, U.S. Customs and Border Protection, or any designee of either such entity.\n##### (c) Limited exception\nNotwithstanding subsections (a) and (b), information provided in an application for permanent resident status under section 245B of the Immigration and Nationality Act may be shared with Federal security and law enforcement agencies\u2014\n**(1)**\nfor assistance in the consideration of an application for permanent resident status under such section;\n**(2)**\nto identify or prevent fraudulent claims;\n**(3)**\nfor national security purposes; or\n**(4)**\nfor the investigation or prosecution of any felony not related to immigration status.\n##### (d) Penalty\nAny person who knowingly uses, publishes, or permits information to be examined in violation of this section shall be fined not more than $10,000.\n#### 4. Additional reporting requirements regarding future discontinued eligibility of aliens from countries currently listed under temporary protected status\nSection 244(b)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking Attorney General each place such term appears and inserting Secretary of Homeland Security ; and\n**(B)**\nby inserting (including a recommendation from the Secretary of State that is received by the Secretary of Homeland Security not later than 90 days before the end of such period of designation) after Government ; and\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby striking If the Attorney General and inserting the following:\n(i) In general If the Secretary of Homeland Security ; and\n**(B)**\nin clause (i), as designated by subparagraph (A), by striking Attorney General and inserting Secretary ; and\n**(C)**\nby adding at the end the following:\n(ii) Report Not later than 3 days after the publication of the Secretary\u2019s determination in the Federal Register that a country\u2019s designation under paragraph (1) is being terminated, the Secretary shall submit a report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives that includes\u2014 (I) an explanation of the event or events that initially prompted such country\u2019s designation under paragraph (1); (II) the progress the country has made in remedying the designation under paragraph (1), including any significant challenges or shortcomings that have not been addressed since the initial designation; (III) a statement indicating whether the country has requested a designation under paragraph (1), a redesignation under such paragraph, or an extension of such designation; and (IV) an analysis, with applicable and relevant metrics, as determined by the Secretary, of the country\u2019s ability to repatriate its nationals, including\u2014 (aa) the country\u2019s financial ability to provide for its repatriated citizens; (bb) the country\u2019s financial ability to address the initial designation under paragraph (1) without foreign assistance; (cc) the country\u2019s gross domestic product and per capita gross domestic product per capita; (dd) an analysis of the country\u2019s political stability and its ability to be economically self-sufficient without foreign assistance; (ee) the economic and social impact the repatriation of nationals in possession of temporary protected status would have on the recipient country; and (ff) any additional metrics the Secretary considers necessary. .\n#### 5. Other matters\n##### (a) Application of Immigration and Nationality Act provisions\nExcept as otherwise specifically provided in this Act, the definitions under section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ) shall apply when such terms are used in this Act.\n##### (b) Savings provision\nNothing in this Act, or the amendments made by this Act, may be construed to repeal, amend, alter, modify, effect, or restrict the powers, duties, functions, or authority of the Secretary of Homeland Security in the administration and enforcement of the immigration laws.\n##### (c) Eligibility for other immigration benefits\nAny alien who is eligible to be granted the status of an alien lawfully admitted for permanent residence under section 245B of the Immigration and Nationality Act, as added by section 2, may not be precluded from seeking such status under any other provision of law for which the alien may otherwise be eligible.",
      "versionDate": "2025-06-18",
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
        "name": "Immigration",
        "updateDate": "2025-07-14T14:22:34Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2106is.xml"
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
      "title": "SECURE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SECURE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Environment from Countries Under Repression and Emergency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide a process for granting lawful permanent resident status to aliens from certain countries who meet certain eligibility requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:18:58Z"
    }
  ]
}
```
