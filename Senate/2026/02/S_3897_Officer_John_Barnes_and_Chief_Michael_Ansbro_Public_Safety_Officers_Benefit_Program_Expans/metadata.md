# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3897?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3897
- Title: Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3897
- Origin chamber: Senate
- Introduced date: 2026-02-24
- Update date: 2026-05-21T21:08:32Z
- Update date including text: 2026-05-21T21:08:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in Senate
- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 416.
- Latest action: 2026-02-24: Introduced in Senate

## Actions

- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 416.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3897",
    "number": "3897",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T21:08:32Z",
    "updateDateIncludingText": "2026-05-21T21:08:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 416.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-02-24",
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
      "actionDate": "2026-02-24",
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
            "date": "2026-05-19T22:19:07Z",
            "name": "Reported By"
          },
          {
            "date": "2026-05-14T17:59:09Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-24T20:28:37Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "DE"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "SC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "NC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3897is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3897\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Mrs. Gillibrand (for herself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo revise administrative procedures relating to public safety officers' death benefits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026 .\n#### 2. Eligibility determination for public safety officer benefits\n##### (a) In general\nSection 1205 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10285 ) is amended\u2014\n**(1)**\nin subsection (e)(2)(E), by inserting , including whether the delay is due to the inaction of the claimant or the failure to cooperate of an agency from which information is required after basis for delay ; and\n**(2)**\nby adding at the end the following:\n(f) Notice and interim benefits (1) Notice of missing information Not later than 90 calendar days after receiving a claim filed under this subpart, the Bureau shall notify the claimant or the relevant agency of any missing information required to process the claim. (2) Notice of determination (A) In general Not later than 270 calendar days after receiving a complete claim, the Bureau shall inform the claimant of the Bureau\u2019s determination as to the claimant\u2019s benefit eligibility. (B) Interim benefits as notice Provision of interim benefits under section 1201(d) shall be deemed to be notice under subparagraph (A). (3) Interim benefits (A) Entitlement If the Bureau fails to inform a claimant of the Bureau's determination on or before the date that is 270 calendar days after receiving a complete claim, the Bureau shall issue a single interim benefit payment with respect to the claim, payable only to\u2014 (i) a claimant whose status as an eligible beneficiary is undisputed; or (ii) if beneficiary status remains unresolved, an escrow or fiduciary account, pending final determination under section 1201. (B) Rescission or repayment Any interim benefits paid under this subsection\u2014 (i) shall be credited against any final benefit determination made under section 1201; (ii) shall not be subject to recoupment or affirmative repayment by the Bureau, except in cases of fraud or material misrepresentation; and (iii) shall not be construed to create an entitlement to benefits if the claimant or decedent is determined to be ineligible under this part. (4) Rule of construction Nothing in this subsection shall be construed to\u2014 (A) limit the Bureau's authority to deny a claim for failure to meet statutory eligibility requirements; (B) alter the determination of eligible beneficiaries under section 1201; or (C) require payment of interim benefits to multiple claimants if the statute authorizes payment to only 1 or more mutually exclusive beneficiaries. (g) Outreach The Bureau shall\u2014 (1) conduct outreach efforts on an ongoing basis to ensure that public safety officers and underserved public agencies are aware of the program under this part, including outreach efforts for disabled public safety officers; and (2) include in the outreach efforts under paragraph (1) regular communications with national public safety organizations, public safety agencies, and organizations supporting disabled public safety officers and the families of fallen officers. (h) Summary of backlogged claims Not later than 30 days after publishing the report required under subsection (e)(2), the Bureau shall submit a summary of the information required to be reported under subsection (e)(2)(E) to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives . (i) Audit of backlogged claims On an annual basis, the Comptroller General shall conduct an audit of any pending claims under this part that were submitted to the Bureau more than 1 year before the date on which the audit is commenced, to identify programmatic challenges to the timely processing of death, disability, and educational assistance claims. As part of the audit, the Comptroller General shall also review\u2014 (1) where the claim is in the determination process; (2) the reasons for delay, including any processes, such as legal review, that prevent timely processing of claims; (3) whether the agency has used its subpoena authority for the claims; (4) the frequency of outreach to the claimant and efforts to evaluate and improve the effectiveness of outreach and claims assistance efforts; (5) the efforts of the Bureau of Justice Assistance to implement a claims processing manual to ensure consistency across staff in determining claims; and (6) efforts to evaluate and improve the effectiveness of outreach and claims assistance efforts. .\n##### (b) Subpoena requirement\nSection 1206(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10288(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(B), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) with respect to information or documentation in the possession of a public agency that the Bureau has determined is necessary to adjudicate the claim that the public agency has failed to provide by the date that is 30 days after the date of the Bureau's or the claimant's request to provide the information or documentation, shall issue a subpoena to the public agency to obtain the information or documentation, unless the Bureau has approved an extension not exceeding 60 days. .\n##### (c) Definitions\n**(1) In general**\nSection 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 ) is amended\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting or gainful work as a public safety officer after including sedentary work each place it appears; and\n**(ii)**\nin subparagraph (B)(ii), by striking parapalegic and inserting paraplegic ;\n**(B)**\nby redesignating paragraph (7) as paragraph (8) and paragraphs (8) through (14) as paragraphs (10) through (16), respectively;\n**(C)**\nby inserting after paragraph (6) the following:\n(7) complete claim means any claim that\u2014 (A) contains all required documents from the claimant and the relevant agency for processing; and (B) has been assigned a claim number by the Bureau; ; and\n**(D)**\nby inserting after paragraph (8), as so redesignated, the following:\n(9) gainful work means gainful work activity, as defined in section 416.972 of title 20, Code of Federal Regulations, or successor regulation; .\n**(2) Conforming amendments**\n**(A) Internal Revenue Code**\nSection 402(l)(4)(C) of the Internal Revenue Code of 1986 is amended by striking (9)(A) each place it appears.\n**(B) Title 28**\nSection 1863(b)(5)(B) of title 28, United States Code, is amended by striking section 1203(6) and inserting section 1204 .\n#### 3. Benefits for permanent and partial disability\n##### (a) In general\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) through (q) as subsections (d) through (r), respectively;\n**(2)**\nby inserting after subsection (b) the following:\n(c) Benefits for permanent and partial disability with inability To continue previous work (1) In general In accordance with regulations issued pursuant to this part, in any case in which the Bureau determines that a public safety officer has become permanently, but not totally, disabled as the direct and proximate result of a personal injury sustained in the line of duty that has caused a physical or mental impairment of such severity that the public safety officer is prevented from performing any gainful work as a public safety officer, including if the individual is medically retired by the public safety agency, a benefit shall be payable to the public safety officer (if living on the date on which the determination is made) of half of the amount that would be payable, as of the date such injury was sustained (including as adjusted in accordance with subsection (i), and calculated in accordance with subsection (j)), if such determination were a determination under subsection (a). (2) Progression of disability If, not later than 3 years after the date of sustaining the injury described in paragraph (1), the severity of the impairment of the public safety officer progresses to that of permanent and total disability, as described in subsection (b), the public safety officer may apply for a benefit under that subsection and, if the Bureau determines that a permanent and total disability exists, the Bureau shall pay the public safety officer a benefit in the amount of the benefit to which the public safety officer would have been entitled under that subsection, less any benefit provided under this subsection. (3) Offset in the event of death If a public safety officer who has received a benefit under this subsection subsequently dies as a direct and proximate result of the same line-of-duty injury, any death benefit payable under subsection (a) shall be reduced by the amount of any benefit previously paid under this subsection. (4) Rule of construction (A) Availability of benefits Nothing in this subsection shall be construed to affect the availability of full benefits under subsection (a) or (b), nor shall this subsection apply to temporary disabilities or injuries that do not result in permanent impairment at the time of filing. (B) Determination A determination under this subsection shall not constitute a final determination with respect to eligibility for benefits under subsection (b). ;\n**(3)**\nby striking subsection (d), and inserting the following:\n(d) Interim payment Whenever the Bureau determines upon showing of need and prior to final action that the disability or death of a public safety officer is one with respect to which a benefit will probably be paid, the Bureau may make an interim benefit payment not exceeding $6,000, adjusted in accordance with subsection (i), to the individual entitled to receive a benefit under subsection (a), (b), or (c) of this section. ; and\n**(4)**\nin subsection (j), as so redesignated, by striking subsections (a) and (b) and inserting subsections (a), (b), and (c) .\n##### (b) Technical and conforming amendments\n**(1) In general**\nPart L of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 et seq. ) is amended\u2014\n**(A)**\nin section 1201\u2014\n**(i)**\nin subsection (a), by striking adjusted in accordance with subsection (h), and calculated in accordance with subsection (i) and inserting adjusted in accordance with subsection (i), and calculated in accordance with subsection (j) ;\n**(ii)**\nin subsection (b), by striking adjusted in accordance with subsection (h), and calculated in accordance with subsection (i) and inserting adjusted in accordance with subsection (i), and calculated in accordance with subsection (j) ;\n**(iii)**\nin subsection (d), as so redesignated, by striking subsection (h) and inserting subsection (i) ;\n**(iv)**\nin subsection (e), as so redesignated, by striking subsection (c) and inserting subsection (d) ;\n**(v)**\nin subsection (i), as so redesignated\u2014\n**(I)**\nby striking subsection (c) and inserting subsection (d) ; and\n**(II)**\nby striking subsections (a) and (b) and inserting subsections (a), (b), and (c) ;\n**(vi)**\nin subsection (j), as so redesignated, by striking and total after death or permanent ;\n**(vii)**\nin subsection (m), as so redesignated, by striking subsection (k) and inserting subsection (l) ;\n**(viii)**\nin subsection (n), as so redesignated, by striking subsection (a), (b), or (c) and inserting subsection (a), (b), (c), or (d) ;\n**(ix)**\nin subsection (p)(3), as so redesignated\u2014\n**(I)**\nin the paragraph heading, by striking and total disability and inserting or permanent disability ;\n**(II)**\nin the matter preceding subparagraph (A), by striking subsection (a) or (b) and inserting subsection (a), (b), or (c) ;\n**(III)**\nin subparagraph (A), by striking and total after death or permanent ; and\n**(IV)**\nin subparagraph (B), by striking and total after death or permanent ; and\n**(x)**\nin subsection (r)(2)(A), as so redesignated\u2014\n**(I)**\nby striking subsection (a) or (b) and inserting subsection (a), (b), or (c) ; and\n**(II)**\nby striking and total each place it appears; and\n**(B)**\nin section 1205(e)\u2014\n**(i)**\nin paragraph (2), by striking (f)(3) and inserting (g)(3) ; and\n**(ii)**\nin paragraph (3)(A), by striking (f)(3) and inserting (g)(3) .\n**(2) Other amendments**\n**(A) Public Safety Officer Support Act**\nSection 3(b)(2) of the Public Safety Officer Support Act of 2022 ( 34 U.S.C. 10281 note; Public Law 117\u2013172 ; 136 Stat. 2101) is amended\u2014\n**(i)**\nby striking section 1201(o) and inserting section 1201(p) ; and\n**(ii)**\nby striking January 1, 2019 and inserting January 1, 2018 .\n**(B) Dale Long Public Safety Officers' Benefits Improvements Act of 2012**\nSection 1086(d)(2)(B) of the National Defense Authorization Act for Fiscal Year 2013 ( Public Law 112\u2013239 ; 126 Stat. 1969) is amended by striking Section 1201(k) and inserting Section 1201(l) .\n**(C) USA PATRIOT Act of 2001**\nSection 611(a) of the Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism Act of 2001 ( 34 U.S.C. 10286(a) ) is amended by striking and total after producing permanent .\n**(D) NDAA FY26**\nSection 8204(b)(2) of the National Defense Authorization Act for Fiscal Year 2026 ( Public Law 119\u201360 ) is amended by striking section 1201(p) and inserting section 1201(q) .\n#### 4. Expedited payment for VCF or WTCHP determinations\nSection 1205(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10285(b) ) is amended by adding at the end the following:\n(4) In making determinations under section 1201(a), the Bureau shall, absent clear and convincing evidence to the contrary, as determined by the Bureau, approve any claim if the September 11th Victim Compensation Fund of 2001 ( 49 U.S.C. 40101 note; Public Law 107\u201342 ) (commonly referred to as the VCF ) or the World Trade Center Health Program under title XXXIII of the Public Health Service Act ( 42 U.S.C. 300mm et seq. ) provides a certification of facts that\u2014 (A) the claim is eligible for death benefits under the Victim Compensation Fund; or (B) the cause of claimant's death is a World Trade Center Health Program-related condition. .\n#### 5. Implementation of certain GAO recommendations\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall ensure that the Director of the Bureau of Justice Assistance implements the recommendations provided in the report of the Government Accountability Office entitled Public Safety Officers' Benefits Program: Transparency, Claims Assistance, and Program Management Improvements Needed (GAO\u201324\u2013105549), published on September 27, 2024.\n#### 6. Educational benefits\nNothing in this Act, or the amendments made by this Act shall be construed as expanding or altering any benefits available to dependents under subpart 2 of part L of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 et seq. ).",
      "versionDate": "2026-02-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3897rs.xml",
      "text": "II\nCalendar No. 416\n119th CONGRESS\n2d Session\nS. 3897\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Mrs. Gillibrand (for herself, Mr. Cruz , Mrs. Shaheen , Mr. Coons , Mr. Graham , Mr. Durbin , Ms. Klobuchar , Mr. Tillis , Ms. Hirono , Mr. Blumenthal , Mr. Padilla , Mr. Welch , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 19, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo revise administrative procedures relating to public safety officers' death benefits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026 .\n#### 2. Eligibility determination for public safety officer benefits\n##### (a) In general\nSection 1205 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10285 ) is amended\u2014\n**(1)**\nin subsection (e)(2)(E), by inserting , including whether the delay is due to the inaction of the claimant or the failure to cooperate of an agency from which information is required after basis for delay ; and\n**(2)**\nby adding at the end the following:\n(f) Notice and interim benefits (1) Notice of missing information Not later than 90 calendar days after receiving a claim filed under this subpart, the Bureau shall notify the claimant or the relevant agency of any missing information required to process the claim. (2) Notice of determination (A) In general Not later than 270 calendar days after receiving a complete claim, the Bureau shall inform the claimant of the Bureau\u2019s determination as to the claimant\u2019s benefit eligibility. (B) Interim benefits as notice Provision of interim benefits under section 1201(d) shall be deemed to be notice under subparagraph (A). (3) Interim benefits (A) Entitlement If the Bureau fails to inform a claimant of the Bureau's determination on or before the date that is 270 calendar days after receiving a complete claim, the Bureau shall issue a single interim benefit payment with respect to the claim, payable only to\u2014 (i) a claimant whose status as an eligible beneficiary is undisputed; or (ii) if beneficiary status remains unresolved, an escrow or fiduciary account, pending final determination under section 1201. (B) Rescission or repayment Any interim benefits paid under this subsection\u2014 (i) shall be credited against any final benefit determination made under section 1201; (ii) shall not be subject to recoupment or affirmative repayment by the Bureau, except in cases of fraud or material misrepresentation; and (iii) shall not be construed to create an entitlement to benefits if the claimant or decedent is determined to be ineligible under this part. (4) Rule of construction Nothing in this subsection shall be construed to\u2014 (A) limit the Bureau's authority to deny a claim for failure to meet statutory eligibility requirements; (B) alter the determination of eligible beneficiaries under section 1201; or (C) require payment of interim benefits to multiple claimants if the statute authorizes payment to only 1 or more mutually exclusive beneficiaries. (g) Outreach The Bureau shall\u2014 (1) conduct outreach efforts on an ongoing basis to ensure that public safety officers and underserved public agencies are aware of the program under this part, including outreach efforts for disabled public safety officers; and (2) include in the outreach efforts under paragraph (1) regular communications with national public safety organizations, public safety agencies, and organizations supporting disabled public safety officers and the families of fallen officers. (h) Summary of backlogged claims Not later than 30 days after publishing the report required under subsection (e)(2), the Bureau shall submit a summary of the information required to be reported under subsection (e)(2)(E) to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives . (i) Audit of backlogged claims On an annual basis, the Comptroller General shall conduct an audit of any pending claims under this part that were submitted to the Bureau more than 1 year before the date on which the audit is commenced, to identify programmatic challenges to the timely processing of death, disability, and educational assistance claims. As part of the audit, the Comptroller General shall also review\u2014 (1) where the claim is in the determination process; (2) the reasons for delay, including any processes, such as legal review, that prevent timely processing of claims; (3) whether the agency has used its subpoena authority for the claims; (4) the frequency of outreach to the claimant and efforts to evaluate and improve the effectiveness of outreach and claims assistance efforts; (5) the efforts of the Bureau of Justice Assistance to implement a claims processing manual to ensure consistency across staff in determining claims; and (6) efforts to evaluate and improve the effectiveness of outreach and claims assistance efforts. .\n##### (b) Subpoena requirement\nSection 1206(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10288(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(B), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) with respect to information or documentation in the possession of a public agency that the Bureau has determined is necessary to adjudicate the claim that the public agency has failed to provide by the date that is 30 days after the date of the Bureau's or the claimant's request to provide the information or documentation, shall issue a subpoena to the public agency to obtain the information or documentation, unless the Bureau has approved an extension not exceeding 60 days. .\n##### (c) Definitions\n**(1) In general**\nSection 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 ) is amended\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting or gainful work as a public safety officer after including sedentary work each place it appears; and\n**(ii)**\nin subparagraph (B)(ii), by striking parapalegic and inserting paraplegic ;\n**(B)**\nby redesignating paragraph (7) as paragraph (8) and paragraphs (8) through (14) as paragraphs (10) through (16), respectively;\n**(C)**\nby inserting after paragraph (6) the following:\n(7) complete claim means any claim that\u2014 (A) contains all required documents from the claimant and the relevant agency for processing; and (B) has been assigned a claim number by the Bureau; ; and\n**(D)**\nby inserting after paragraph (8), as so redesignated, the following:\n(9) gainful work means gainful work activity, as defined in section 416.972 of title 20, Code of Federal Regulations, or successor regulation; .\n**(2) Conforming amendments**\n**(A) Internal Revenue Code**\nSection 402(l)(4)(C) of the Internal Revenue Code of 1986 is amended by striking (9)(A) each place it appears.\n**(B) Title 28**\nSection 1863(b)(5)(B) of title 28, United States Code, is amended by striking section 1203(6) and inserting section 1204 .\n#### 3. Benefits for permanent and partial disability\n##### (a) In general\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) through (q) as subsections (d) through (r), respectively;\n**(2)**\nby inserting after subsection (b) the following:\n(c) Benefits for permanent and partial disability with inability To continue previous work (1) In general In accordance with regulations issued pursuant to this part, in any case in which the Bureau determines that a public safety officer has become permanently, but not totally, disabled as the direct and proximate result of a personal injury sustained in the line of duty that has caused a physical or mental impairment of such severity that the public safety officer is prevented from performing any gainful work as a public safety officer, including if the individual is medically retired by the public safety agency, a benefit shall be payable to the public safety officer (if living on the date on which the determination is made) of half of the amount that would be payable, as of the date such injury was sustained (including as adjusted in accordance with subsection (i), and calculated in accordance with subsection (j)), if such determination were a determination under subsection (a). (2) Progression of disability If, not later than 3 years after the date of sustaining the injury described in paragraph (1), the severity of the impairment of the public safety officer progresses to that of permanent and total disability, as described in subsection (b), the public safety officer may apply for a benefit under that subsection and, if the Bureau determines that a permanent and total disability exists, the Bureau shall pay the public safety officer a benefit in the amount of the benefit to which the public safety officer would have been entitled under that subsection, less any benefit provided under this subsection. (3) Offset in the event of death If a public safety officer who has received a benefit under this subsection subsequently dies as a direct and proximate result of the same line-of-duty injury, any death benefit payable under subsection (a) shall be reduced by the amount of any benefit previously paid under this subsection. (4) Rule of construction (A) Availability of benefits Nothing in this subsection shall be construed to affect the availability of full benefits under subsection (a) or (b), nor shall this subsection apply to temporary disabilities or injuries that do not result in permanent impairment at the time of filing. (B) Determination A determination under this subsection shall not constitute a final determination with respect to eligibility for benefits under subsection (b). ;\n**(3)**\nby striking subsection (d), and inserting the following:\n(d) Interim payment Whenever the Bureau determines upon showing of need and prior to final action that the disability or death of a public safety officer is one with respect to which a benefit will probably be paid, the Bureau may make an interim benefit payment not exceeding $6,000, adjusted in accordance with subsection (i), to the individual entitled to receive a benefit under subsection (a), (b), or (c) of this section. ; and\n**(4)**\nin subsection (j), as so redesignated, by striking subsections (a) and (b) and inserting subsections (a), (b), and (c) .\n##### (b) Technical and conforming amendments\n**(1) In general**\nPart L of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 et seq. ) is amended\u2014\n**(A)**\nin section 1201\u2014\n**(i)**\nin subsection (a), by striking adjusted in accordance with subsection (h), and calculated in accordance with subsection (i) and inserting adjusted in accordance with subsection (i), and calculated in accordance with subsection (j) ;\n**(ii)**\nin subsection (b), by striking adjusted in accordance with subsection (h), and calculated in accordance with subsection (i) and inserting adjusted in accordance with subsection (i), and calculated in accordance with subsection (j) ;\n**(iii)**\nin subsection (d), as so redesignated, by striking subsection (h) and inserting subsection (i) ;\n**(iv)**\nin subsection (e), as so redesignated, by striking subsection (c) and inserting subsection (d) ;\n**(v)**\nin subsection (i), as so redesignated\u2014\n**(I)**\nby striking subsection (c) and inserting subsection (d) ; and\n**(II)**\nby striking subsections (a) and (b) and inserting subsections (a), (b), and (c) ;\n**(vi)**\nin subsection (j), as so redesignated, by striking and total after death or permanent ;\n**(vii)**\nin subsection (m), as so redesignated, by striking subsection (k) and inserting subsection (l) ;\n**(viii)**\nin subsection (n), as so redesignated, by striking subsection (a), (b), or (c) and inserting subsection (a), (b), (c), or (d) ;\n**(ix)**\nin subsection (p)(3), as so redesignated\u2014\n**(I)**\nin the paragraph heading, by striking and total disability and inserting or permanent disability ;\n**(II)**\nin the matter preceding subparagraph (A), by striking subsection (a) or (b) and inserting subsection (a), (b), or (c) ;\n**(III)**\nin subparagraph (A), by striking and total after death or permanent ; and\n**(IV)**\nin subparagraph (B), by striking and total after death or permanent ; and\n**(x)**\nin subsection (r)(2)(A), as so redesignated\u2014\n**(I)**\nby striking subsection (a) or (b) and inserting subsection (a), (b), or (c) ; and\n**(II)**\nby striking and total each place it appears; and\n**(B)**\nin section 1205(e)\u2014\n**(i)**\nin paragraph (2), by striking (f)(3) and inserting (g)(3) ; and\n**(ii)**\nin paragraph (3)(A), by striking (f)(3) and inserting (g)(3) .\n**(2) Other amendments**\n**(A) Public Safety Officer Support Act**\nSection 3(b)(2) of the Public Safety Officer Support Act of 2022 ( 34 U.S.C. 10281 note; Public Law 117\u2013172 ; 136 Stat. 2101) is amended\u2014\n**(i)**\nby striking section 1201(o) and inserting section 1201(p) ; and\n**(ii)**\nby striking January 1, 2019 and inserting January 1, 2018 .\n**(B) Dale Long Public Safety Officers' Benefits Improvements Act of 2012**\nSection 1086(d)(2)(B) of the National Defense Authorization Act for Fiscal Year 2013 ( Public Law 112\u2013239 ; 126 Stat. 1969) is amended by striking Section 1201(k) and inserting Section 1201(l) .\n**(C) USA PATRIOT Act of 2001**\nSection 611(a) of the Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism Act of 2001 ( 34 U.S.C. 10286(a) ) is amended by striking and total after producing permanent .\n**(D) NDAA FY26**\nSection 8204(b)(2) of the National Defense Authorization Act for Fiscal Year 2026 ( Public Law 119\u201360 ) is amended by striking section 1201(p) and inserting section 1201(q) .\n#### 4. Expedited payment for VCF or WTCHP determinations\nSection 1205(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10285(b) ) is amended by adding at the end the following:\n(4) In making determinations under section 1201(a), the Bureau shall, absent clear and convincing evidence to the contrary, as determined by the Bureau, approve any claim if the September 11th Victim Compensation Fund of 2001 ( 49 U.S.C. 40101 note; Public Law 107\u201342 ) (commonly referred to as the VCF ) or the World Trade Center Health Program under title XXXIII of the Public Health Service Act ( 42 U.S.C. 300mm et seq. ) provides a certification of facts that\u2014 (A) the claim is eligible for death benefits under the Victim Compensation Fund; or (B) the cause of claimant's death is a World Trade Center Health Program-related condition. .\n#### 5. Implementation of certain GAO recommendations\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall ensure that the Director of the Bureau of Justice Assistance implements the recommendations provided in the report of the Government Accountability Office entitled Public Safety Officers' Benefits Program: Transparency, Claims Assistance, and Program Management Improvements Needed (GAO\u201324\u2013105549), published on September 27, 2024.\n#### 6. Educational benefits\nNothing in this Act, or the amendments made by this Act shall be construed as expanding or altering any benefits available to dependents under subpart 2 of part L of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 et seq. ).",
      "versionDate": "2026-05-19",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-02-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7718",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Officer John Barnes and Chief Michael Ansbro Public Safety Officers\u2019 Benefits Program Expansion Act of 2026",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-13T15:08:59Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3897is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3897rs.xml"
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
      "title": "Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-21T21:08:32Z"
    },
    {
      "title": "Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Officer John Barnes and Chief Michael Ansbro Public Safety Officers' Benefit Program Expansion Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to revise administrative procedures relating to public safety officers' death benefits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T03:18:25Z"
    }
  ]
}
```
