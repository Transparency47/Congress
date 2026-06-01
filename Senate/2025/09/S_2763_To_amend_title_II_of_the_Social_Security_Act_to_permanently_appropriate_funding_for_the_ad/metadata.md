# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2763?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2763
- Title: Keep Billionaires Out of Social Security Act
- Congress: 119
- Bill type: S
- Bill number: 2763
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2025-09-23T15:40:34Z
- Update date including text: 2025-09-23T15:40:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2763",
    "number": "2763",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Keep Billionaires Out of Social Security Act",
    "type": "S",
    "updateDate": "2025-09-23T15:40:34Z",
    "updateDateIncludingText": "2025-09-23T15:40:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T21:07:18Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "OR"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-09-10",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "DE"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "WI"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "IL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CO"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "RI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "WA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NM"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2763is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2763\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Sanders (for himself, Mr. Wyden , Mr. Schumer , Mr. Blumenthal , Mrs. Gillibrand , Ms. Smith , Ms. Warren , Mr. Reed , Mr. Kim , Mr. Markey , Mr. King , Mr. Welch , Ms. Klobuchar , Mr. Coons , Ms. Baldwin , Ms. Hirono , Mr. Padilla , Mr. Durbin , Mr. Hickenlooper , Mr. Van Hollen , Mr. Merkley , Mr. Whitehouse , Mr. Kaine , Mr. Gallego , Mr. Bennet , Mr. Booker , Mrs. Murray , Mr. Warner , Ms. Alsobrooks , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title II of the Social Security Act to permanently appropriate funding for the administrative expenses of the Social Security Administration, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Keep Billionaires Out of Social Security Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Exempting Social Security from the jurisdiction of the Department of Government Efficiency (DOGE) and the application of certain executive orders.\nSec. 3. Access by political appointees and special government employees.\nSec. 4. Limitations on authority of Social Security Administration to except positions from competitive service and transfer positions.\nSec. 5. Requiring that only deceased individuals be added to the Death Master File.\nSec. 6. Closure of field and hearing offices and resident or rural contact stations.\nSec. 7. Reestablishing the Offices of Civil Rights and Equal Opportunity, Transformation, and Analytics, Review, and Oversight.\nSec. 8. Funding for administrative expenses of the Social Security Administration.\nSec. 9. Additional funding to improve Social Security customer experience.\nSec. 10. Codification of former policy regarding recovery of Social Security overpayments.\nSec. 11. State grants to protect the legal rights of SSI and SSDI applicants and beneficiaries.\nSec. 12. Social Security assistance and representation grants.\n#### 2. Exempting Social Security from the jurisdiction of the Department of Government Efficiency (DOGE) and the application of certain executive orders\n##### (a) In general\nWith respect to the agencies, personnel, systems, and benefits and programs described in subsection (b)\u2014\n**(1)**\nDOGE shall have no authority or jurisdiction; and\n**(2)**\nthe Executive orders described in subsection (c) shall not apply.\n##### (b) Covered agencies, personnel, systems, and benefits and programs\nThe agencies, personnel, systems, and benefits and programs described in this subsection are the Social Security Administration, any officer or employee of the Social Security Administration, the data, information technology, and operating systems of the Social Security Administration, and any benefits or program administered by the Social Security Administration, including the Old-Age and Survivors Insurance and Disability Insurance programs and associated benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ).\n##### (c) Executive orders\nThe Executive orders described in this subsection are\u2014\n**(1)**\nExecutive Orders 14158, 14210, 14219, and 14222 (90 Fed. Reg. 8441, 9669, 10583, 11095); and\n**(2)**\nany other Executive order relating to any entity described in paragraph (1), (2), (3), or (5).\n##### (d) DOGE\nFor purposes of this section, the term DOGE means\u2014\n**(1)**\nthe United States DOGE Service;\n**(2)**\nthe United States DOGE Service Temporary Organization;\n**(3)**\nany DOGE team (as defined in any of the Executive orders described in subsection (c)(1));\n**(4)**\nany entity established in accordance with, or to implement, any Executive order described in subsection (c); and\n**(5)**\nany successor entity to an entity described in paragraphs (1) through (4).\n#### 3. Access by political appointees and special government employees\n##### (a) In general\nSection 1106 of the Social Security Act ( 42 U.S.C. 1306 ) is amended by adding after subsection (g) the following new subsections:\n(h) Access by political appointees and special government employees (1) In general (A) Prohibition on access to beneficiary data systems Notwithstanding any other subsection of this section, an individual who is a political appointee (as that term is defined in section 4(a) of the Edward \u2018Ted\u2019 Kaufman and Michael Leavitt Presidential Transitions Improvements Act of 2015 ( 5 U.S.C. 3101 note)) or a special government employee (as that term is defined in section 202(a) of title 18, United States Code) may not access a beneficiary data system. (B) Exception Subparagraph (A) shall not apply with respect to a political appointee or special government employee who has been appointed to, or is employed in, a position within the Social Security Administration with responsibility to research, analyze, or improve the delivery of benefits to program recipients. (2) Beneficiary data system defined In this section, the term beneficiary data system means a system that is maintained by the Social Security Administration for the purposes of administering this Act that\u2014 (A) issues or records social security account numbers; (B) is used to determine eligibility for benefits under this Act; (C) to pay benefits under this Act; or (D) otherwise contains records of personally identifiable information, personal health information, or Federal tax information of individuals receiving or applying for a benefit under this Act. (i) Civil penalties (1) In general (A) Disclosure or access by employee of United States If any officer or employee of the United States negligently discloses or accesses any information that pertains to an individual in violation of any provision of subsection (a) or (h), such individual may bring a civil action for damages against the United States in a district court of the United States. (B) Disclosure or access by a person who is not an employee of United States If any person who is not an officer or employee of the United States negligently discloses or accesses any information that pertains to an individual in violation of any provision of subsection (a) or (h), such individual may bring a civil action for damages against such person in a district court of the United States. (2) Exceptions No liability shall arise under this section with respect to any disclosure or access\u2014 (A) which results from a good faith, but erroneous, interpretation of subsection (a) or (h); or (B) which is requested by the individual. (3) Damages In any action brought under paragraph (1), upon a finding of liability on the part of the defendant, the defendant shall be liable to the plaintiff in an amount equal to the sum of\u2014 (A) the greater of\u2014 (i) $5,000 for each act of unauthorized access or disclosure with respect to which such defendant is found liable; or (ii) the sum of\u2014 (I) the actual damages sustained by the plaintiff as a result of such unauthorized access or disclosure, plus (II) in the case of a willful access or disclosure or an access or disclosure which is the result of gross negligence, punitive damages, (B) the costs of the action, plus (C) reasonable attorneys fees, except that if the defendant is the United States, reasonable attorneys fees may be awarded only if the plaintiff is the prevailing party. (4) Period for bringing action Notwithstanding any other provision of law, an action to enforce any liability created under this section may be brought, without regard to the amount in controversy, at any time within 5 years after the date of discovery by the plaintiff of the unauthorized disclosure or access. (j) Criminal penalties It shall be unlawful for any officer or employee of the United States to willfully to disclose to any person any information that pertains to an individual in violation of any provision of subsection (a) or (h). Any violation of this subsection shall be a felony punishable upon conviction by a fine in any amount not exceeding $10,000, or imprisonment of not more than 5 years, or both, together with the costs of prosecution, and, in addition to any other punishment, such officer or employee shall be dismissed from office or discharged from employment upon conviction for such offense. (k) Investigation and report (1) Investigation The Inspector General of the Social Security Administration shall investigate each disclosure in violation of subsection (a) and each access of a beneficiary data system in violation of subsection (h). (2) Treatment of disclosure or access For the purposes of this subsection, the Inspector General may, if the Inspector General determines appropriate, treat a series of violations of subsection (a) or (h) as a single violation. (3) Report Not later than 30 days after the Inspector General becomes aware of a violation of subsection (a) or (h), the Inspector General shall submit to Congress a report on such violation, which shall include\u2014 (A) a detailed description of the violation; (B) a risk assessment of any threat to the privacy of any individual whose information was disclosed or accessed, national security, cybersecurity, or the integrity of the applicable beneficiary data system as a result of the violation; and (C) a detailed description of any stopped payment during the unauthorized use or access. .\n##### (b) Privacy regulations\nNotwithstanding this section and the amendments made by this section, part 401 of title 20 of the Code of Federal Regulations, as in effect on January 19, 2025, shall have the force and effect of law.\n##### (c) GAO study and interim reports\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Comptroller of the United States shall submit to the Committee on Finance of the Senate and the Committee on Ways and Means of the House of Representatives a report including the following information:\n**(A)**\nThe results of a study on the effects of the changes made to section 1106 of the Social Security Act ( 42 U.S.C. 1306 ) by this section and any subsequently enacted law.\n**(B)**\nAny civil actions brought under subsection (i) of section 1106 of such Act, as added by subsection (a), including the results of such civil action.\n**(C)**\nA summary of any investigations conducted under subsection (k) of section 1106 of such Act, as added by subsection (a).\n**(D)**\nAny convictions for a violation of subsection (a) or (h) of section 1106 of such Act under subsection (j) of such Act, as added by subsection (a).\n**(2) Interim reports**\nNot later than 1 month after the date of enactment of this Act, and monthly thereafter until such time as the report required under paragraph (1) is submitted, the Comptroller of the United States shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate an interim report on the information required under paragraph (1), including the status of the study described in subparagraph (A) of such paragraph.\n##### (d) Effective date\nThe amendments made by subsections (a) and (b) of this section shall apply to violations of section 1106 of the Social Security Act occurring on or after the date of enactment of this Act.\n#### 4. Limitations on authority of Social Security Administration to except positions from competitive service and transfer positions\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term Administration means the Social Security Administration;\n**(2)**\nthe term Commissioner means the Commissioner of Social Security;\n**(3)**\nthe term competitive service has the meaning given the term in section 2102 of title 5, United States Code;\n**(4)**\nthe term Director means the Director of the Office of Personnel Management; and\n**(5)**\nthe term excepted service has the meaning given the term in section 2103 of title 5, United States Code.\n##### (b) Limitations\nA position in the competitive service in the Administration may not be excepted from the competitive service unless that position is placed\u2014\n**(1)**\nin any of schedules A through E, as described in section 6.2 of title 5, Code of Federal Regulations, as in effect on September 30, 2020; and\n**(2)**\nunder the terms and conditions under part 6 of title 5, Code of Federal Regulations, as in effect on September 30, 2020.\n##### (c) Transfers\n**(1) Within excepted service**\nA position in the excepted service in the Administration may not be transferred to any schedule other than a schedule described in subsection (b)(1).\n**(2) OPM consent required**\nThe Commissioner may not transfer any occupied position in the Administration from the competitive service or the excepted service into schedule C of subpart C of part 213 of title 5, Code of Federal Regulations, or any successor regulations, without the prior consent of the Director.\n**(3) Limit during presidential term**\nDuring any 4-year presidential term, the Commissioner may not transfer from a position in the competitive service in the Administration to a position in the excepted service in the Administration the greater of the following:\n**(A)**\nA total number of employees that is more than 1 percent of the total number of employees employed by the Administration, as of the first day of that presidential term.\n**(B)**\n5 employees.\n**(4) Employee consent required**\nNotwithstanding any other provision of this section\u2014\n**(A)**\nan employee who occupies a position in the excepted service in the Administration may not be transferred to an excepted service schedule other than the schedule in which that position is located without the prior written consent of the employee; and\n**(B)**\nan employee who occupies a position in the competitive service in the Administration may not be transferred to the excepted service without the prior written consent of the employee.\n##### (d) Report\nNot later than March 15 of each calendar year, the Director shall submit to Congress a report on the immediately preceding calendar year that lists\u2014\n**(1)**\neach position in the Administration that, during the year covered by the report, was transferred from the competitive service to the excepted service and a justification as to why each such position was so transferred; and\n**(2)**\nany violation of this section that occurred during the year covered by the report.\n##### (e) Regulations\nNot later than 90 days after the date of enactment of this Act, the Director shall issue regulations to implement this section.\n#### 5. Requiring that only deceased individuals be added to the Death Master File\nSection 205(r) of the Social Security Act ( 42 U.S.C. 405(r) ) is amended\u2014\n**(1)**\nin paragraph (7)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking may and inserting shall ;\n**(B)**\nin subparagraph (A), by striking and ;\n**(C)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(C) notify any agency that has a cooperative arrangement with the Commissioner of Social Security under paragraph (3) or (11) of the error. ; and\n**(2)**\nby adding at the end the following new paragraph:\n(12) The Commissioner of Social Security may not record a death to a record that may be provided under this section for any individual unless the Commissioner of Social Security has found it has clear and convincing evidence to support that the individual should be presumed to be deceased. .\n#### 6. Closure of field and hearing offices and resident or rural contact stations\n##### (a) In general\nSection 704 of the Social Security Act ( 42 U.S.C. 904 ) is amended by adding at the end the following new subsection:\n(f) Access to Field and Hearing Offices and Live Telephone Operator Services (1) The Commissioner of Social Security shall\u2014 (A) maintain, at a minimum, the same number of field and hearing offices of the Social Security Administration that existed on January 1, 2025; (B) not close, or reduce the level of services provided by, any field office, hearing office, or resident station of the Administration that existed on January 1, 2025, except in the case of a short-term emergency or relocation; (C) maintain meaningful and efficient access to live operator assistance; and (D) not later than 12 months after the date of enactment of the Keep Billionaires Out of Social Security Act , significantly improve telephone wait times, callback times, and average service times for beneficiaries and applicants, as compared to the average levels for such times during calendar year 2024. (2) The Commissioner may make recommendations to Congress proposing field or hearing office location changes, consolidations, or closures from time to time. (3) The Commissioner may\u2014 (A) establish new field or hearing offices in addition to those that existed on January 1, 2025; and (B) expand the level of services offered by a field or hearing office beyond what such office offered on January 1, 2025. (4) The Commissioner shall not limit public access to any field or hearing office of the Administration, or the staff of any such office, that existed on January 1, 2025. (5) The Commissioner shall not reduce the number of employees of the Administration (as determined on an annual basis) below the number of employees of the Administration that were employed during calendar year 2024. (6) The Administration shall not be subject to any hiring freeze, hiring prohibition, reduction in force order, or similar policy, and, notwithstanding any such freeze, prohibition, order, or policy, the Commissioner shall have the authority to hire new employees if the Commissioner deems it necessary to improve services provided by the Administration to beneficiaries and applicants of the programs established under this Act. (7) The Commissioner shall establish an online option, in accessible formats, for beneficiaries and applicants to apply, make benefit claims, and make changes to direct deposit information. .\n##### (b) Retroactive application\nThe amendment made by this section shall take effect as if enacted on January 1, 2025, and any actions taken by the Commissioner of Social Security or any other officer of the executive branch that are inconsistent with such amendment shall be reversed.\n#### 7. Reestablishing the Offices of Civil Rights and Equal Opportunity, Transformation, and Analytics, Review, and Oversight\nSection 702 of the Social Security Act ( 42 U.S.C. 902 ) is amended by adding at the end the following new subsections:\n(f) Civil Rights and Equal Opportunity (1) In general There shall be in the Administration an Office of Civil Rights and Equal Opportunity. The head of the Office of Civil Rights and Equal Opportunity shall be the Deputy Commissioner of Civil Rights, who shall\u2014 (A) be appointed by the Commissioner; (B) as of the date on which the appointment described in subparagraph (A) is made, be serving as a career appointee (as defined in section 3132(a) of title 5, United States Code) in the Social Security Administration; and (C) exercise such duties as are appropriate for the Office of Civil Rights and Equal Opportunity of the Administration and in accordance with Federal civil rights laws. (2) Responsibilities The Office of Civil Rights and Equal Opportunity shall be responsible for the management of the Administration\u2019s programs of civil rights and equal opportunity, including the development of the Administration\u2019s civil rights and equal opportunity policies, regulations, procedures, and enforcement of the Americans with Disabilities Act of 1990 and sections 501, 504, and 505 of the Rehabilitation Act of 1973 pertaining to the development of affirmative action employment and equal opportunity programs to cultivate a diverse and inclusive environment, which shall include\u2014 (A) planning, implementing, and directing programs designed to ensure equal opportunity in employment for all employees regardless of race, color, national origin, religion, age, disability, genetic information, or sex; (B) processing, adjudicating, and resolving complaints of discrimination in compliance with all applicable laws, regulations, and other guidance issued by the Equal Employment Opportunity Commission; (C) directing and managing the Administration\u2019s reasonable accommodation program for employees with disabilities; and (D) developing and maintaining all necessary information systems to manage the Administration's equal opportunity programs, develop reliable statistical data analyses, and track workloads. (g) Transformation There shall be in the Administration an Office of Transformation. The head of the Office of Transformation shall be the Deputy Commissioner of Transformation, who shall\u2014 (1) be appointed by the Commissioner; (2) as of the date on which the appointment described in paragraph (1) is made, be serving as a career appointee (as defined in section 3132(a) of title 5, United States Code) in the Social Security Administration; and (3) exercise such duties as are appropriate for the Office of Transformation of the Administration, which shall include strategic guidance and oversight of the Administration\u2019s initiatives, addressing policies, business processes, and systems, including customer service-related systems and projects and resolving delays and ensure successful implementation of such systems and projects. (h) Analytics, Review, and Oversight There shall be in the Administration an Office of Analytics, Review, and Oversight. The head of the Office of Analytics, Review, and Oversight shall be the Deputy Commissioner of Analytics, Review, and Oversight, who shall\u2014 (1) be appointed by the Commissioner; (2) as of the date on which the appointment described in paragraph (1) is made, be serving as a career appointee (as defined in section 3132(a) of title 5, United States Code) in the Social Security Administration; (3) exercise such duties as are appropriate for the Office of Analytics, Review, and Oversight of the Administration which shall include reviewing program quality and effectiveness, making recommendations for program improvement, and coordinating the detection and prevention of fraud. .\n#### 8. Funding for administrative expenses of the Social Security Administration\n##### (a) In general\nSection 201(g)(1)(A) of the Social Security Act ( 42 U.S.C. 401(g)(1)(A) ) is amended\u2014\n**(1)**\nin the third sentence of the matter following clause (ii), by striking the costs of the part of the administration of this title, title VIII, title XVI, and title XVIII for which the Commissioner of Social Security is responsible, ; and\n**(2)**\nby adding at the end the following: For each fiscal year beginning with fiscal year 2026, there is hereby appropriated to pay the costs of the part of the administration of this title, title VIII, and title XVI for which the Commissioner of Social Security is responsible an amount equal to 1.2 percent of the sum of the amount of benefit payments required to be made under this title for the fiscal year involved and the amount of benefit payments expected to be paid under titles VIII and XVI for the fiscal year involved, as estimated by the Chief Actuary of the Social Security Administration. For purposes of the preceding sentence, (I) the portion of the amount to be appropriated for a fiscal year that is attributable to benefit payments required to be made under this title shall be appropriated from the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund, in such proportion as the Commissioner of Social Security shall determine, and (II) the portion of the amount to be appropriated for a fiscal year that is attributable to benefit payments expected to be made under titles VIII and XVI shall be appropriated from the general fund of the Treasury. For each fiscal year beginning with fiscal year 2026, there is hereby appropriated from the Federal Hospital Insurance Trust Fund and the Federal Supplementary Medical Insurance Trust Fund, in such proportion as the Administrator of the Centers for Medicare & Medicaid Services shall determine, such sums as are necessary to pay the costs of the part of the administration of title XVIII for which the Commissioner of Social Security is responsible. .\n##### (b) Removing the limitation on the administrative expenses of the Social Security Administration from discretionary budget caps, the Congressional Budget Resolution, the 302(a) allocations and the 302(b) suballocations\n**(1) Exclusion of the administrative costs of Social Security, SSI, and parts of Medicare from all budgets**\nSection 13301(a) of the Budget Enforcement Act of 1990 ( 2 U.S.C. 632 note) is amended to read as follows:\n(a) Exclusion of the administrative costs of Social Security, SSI, and parts of Medicare from all budgets (1) In general Notwithstanding any other provision of law, the receipts and disbursements described in paragraph (2) and the costs of program integrity activities described in paragraph (3) shall not be counted as new budget authority, outlays, receipts, or deficit or surplus for purposes of\u2014 (A) the budget of the United States Government as submitted by the President under section 1105 of title 31, United States Code; (B) a concurrent resolution on the budget; (C) the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900 et seq. ); or (D) the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 931 et seq. ). (2) Receipts and disbursements covered The receipts and disbursements described in this paragraph are\u2014 (A) the receipts and disbursements of the Federal Old-Age and Survivors Trust Fund and the Federal Disability Insurance Trust Fund, including the costs of the part of the administration of title II of the Social Security Act for which the Commissioner of Social Security is responsible; and (B) the receipts and disbursements from the Federal Hospital Insurance Trust Fund, the Federal Supplementary Insurance Trust Fund, and amounts appropriated for the Supplemental Security Income program and for benefits paid to certain World War II veterans under title VIII of the Social Security Act for the costs of the part of the administration of titles VIII, XVI, and XVIII of such Act for which the Commissioner of Social Security is responsible. (3) Program integrity activities The costs of program integrity activities described in this paragraph are costs associated with\u2014 (A) continuing disability reviews under titles II and XVI of the Social Security Act; (B) conducting redeterminations of eligibility under title XVI of such Act; (C) cooperative disability investigation units; and (D) the prosecution of fraud in the programs and operations of the Social Security Administration by Special Assistant United States Attorneys. .\n**(2) Exclusion of the administrative costs of Social Security, SSI, and parts of Medicare from the Congressional Budget Resolution**\nSection 301(a) of the Congressional Budget Act of 1974 ( 2 U.S.C. 632(a) ) is amended by striking the matter following paragraph (7) and inserting the following:\nThe concurrent resolution shall not include in the surplus or deficit totals required by this subsection or in any other surplus or deficit totals required by this title the outlays and revenue totals of the program under title II of the Social Security Act, or the related provisions of the Internal Revenue Code of 1986, including the costs of the part of the administration of such title II for which the Commissioner of Social Security is responsible or the costs of the part of the administration of titles XVI and XVIII of the Social Security Act for which the Commissioner of Social Security is responsible. .\n**(3) Exclusion of the administrative costs of Social Security, SSI, and parts of Medicare from Congressional Budget Act 302(a) allocations**\nSection 302(a)(1) of the Congressional Budget Act of 1974 ( 2 U.S.C. 633(a)(1) ) is amended by adding at the end the following: The allocation under this paragraph shall not include the outlays of the program under title II of the Social Security Act, including the costs of the part of the administration of such title for which the Commissioner of Social Security is responsible, or the outlays for the costs of the part of the administration of titles XVI and XVIII of the Social Security Act for which the Commissioner of Social Security is responsible. .\n**(4) Exclusion of the administrative costs of Social Security, SSI, and parts of Medicare from the Congressional Budget Act 302(b) suballocations**\nSection 302(b) of the Congressional Budget Act of 1974 ( 2 U.S.C. 633(b) ) is amended by adding at the end the following: The suballocation under this subsection shall not include the outlays of the program under title II of the Social Security Act, including the costs of the part of the administration of such title for which the Commissioner of Social Security is responsible, or the outlays for the costs of the part of the administration of titles XVI and XVIII of the Social Security Act for which the Commissioner of Social Security is responsible. .\n##### (c) Rule of construction\nNothing in this section, or the amendments made by this section, shall be construed to reduce or eliminate the authority of the Committees on Appropriations of the House of Representatives and the Senate to oversee or direct outlays for the costs of the part of the administration under title II of the Social Security Act, or the outlays for the costs of the part of the administration of titles XVI and XVIII of the Social Security Act, for which the Commissioner of Social Security is responsible.\n##### (d) Effective date\nThe amendments made by this section shall take effect on October 1, 2025.\n#### 9. Additional funding to improve Social Security customer experience\n##### (a) In general\nThere are appropriated to the Commissioner of Social Security (referred to in this section as the Commissioner ) for the period of fiscal year 2026 through fiscal year 2035, out of any money in the Treasury not otherwise appropriated, $2,000,000,000, to remain available until expended, to be used by the Commissioner for the following purposes:\n**(1)**\nTo conduct efforts to increase awareness of eligibility for supplemental security income benefits among families with children who may be eligible for such benefits, with such efforts to be conducted throughout the United States to ensure families of children with disabilities have awareness of the program, its eligibility standards, and how to apply.\n**(2)**\nTo reduce the initial disability insurance benefit claims backlog and other disability insurance benefit workloads, as well as backlogs and workloads relating to claims for benefits under title II or XVI of the Social Security Act which involve a disability determination (including appeals), including by directing resources and workload assistance to areas with the greatest need.\n**(3)**\nMaintaining, expanding, modernizing, or enhancing the information technology capabilities and infrastructure of the Social Security Administration, while ensuring that delivery of benefits continues uninterrupted.\n**(4)**\nIncreasing the menu of services that can be performed online, including an application for benefits under title XVI of the Social Security Act.\n##### (b) Reports to Congress\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Commissioner shall submit to Congress a report on the actions being undertaken by the Social Security Administration to address the issues described in paragraphs (1) through (4) of subsection (a).\n#### 10. Codification of former policy regarding recovery of Social Security overpayments\n##### (a) In general\nSection 204(a)(1)(A) of the Social Security Act ( 42 U.S.C. 404(a)(1)(A) ) is amended\u2014\n**(1)**\nby striking With respect to payment and inserting (i) Subject to clause (ii), with respect to payment ; and\n**(2)**\nby adding at the end the following new clause:\n(ii) (I) With respect to adjustment or recovery on account of an overpayment pursuant to clause (i), the amount of any monthly benefit payable to such person under this title shall be decreased by the Commissioner of Social Security by an amount equal to the greater of\u2014 (aa) 10 percent of such monthly benefit, or (bb) $10. (II) Subclause (I) shall not apply in the case of a person who\u2014 (aa) received payment of more than the correct amount as a result of fraud or similar fault (as defined in section 205(u)(2)), or (bb) elects to waive application of such subclause and requests that the Commissioner of Social Security impose a greater decrease in the amount of monthly benefits payable to such person under this title than the amount otherwise determined under such subclause. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to overpayment determinations made on or after March 25, 2024, and to any other overpaid amounts that have not been recovered as of such date.\n#### 11. State grants to protect the legal rights of SSI and SSDI applicants and beneficiaries\nTitle XI of the Social Security Act ( 42 U.S.C. 1301 et seq. ) is amended by inserting after section 1150C the following new section:\n1150D. State grants to protect the legal rights of supplemental security and disability insurance applicants and beneficiaries (a) In general The Commissioner may make payments in each State to the protection and advocacy system established pursuant to part C of title I of the Developmental Disabilities Assistance and Bill of Rights Act for the purpose of protecting the legal rights of beneficiaries with a disability. (b) Services provided Services provided to beneficiaries with a disability pursuant to a payment made under this section may include\u2014 (1) information and advice about accessing and applying for benefits under title II or title XVI on the basis of a disability and appealing eligibility decisions with respect to such benefits; (2) advocacy and other services that a beneficiary with a disability may need related to such benefits; and (3) services described in section 1150(b). (c) Application In order to receive payments under this section, a protection and advocacy system shall submit an application to the Commissioner, at such time, in such form and manner, and accompanied by such information and assurances as the Commissioner may require. (d) Amount of payments (1) In general Subject to the amount appropriated for a fiscal year for making payments under this section, a protection and advocacy system shall not be paid an amount that is less than\u2014 (A) in the case of a protection and advocacy system located in one of the 50 States, the District of Columbia, or Puerto Rico, $200,000; and (B) in the case of a protection and advocacy system located in Guam, American Samoa, the United States Virgin Islands, or the Commonwealth of the Northern Mariana Islands, $100,000. (2) Inflation adjustment For each fiscal year in which the total amount appropriated to carry out this section exceeds the total amount appropriated to carry out this section in the preceding fiscal year, the Commissioner shall increase each minimum payment under subparagraphs (A) and (B) of paragraph (1) by a percentage equal to the percentage increase in the total amount so appropriated to carry out this section. (e) Annual report Each protection and advocacy system that receives a payment under this section shall submit an annual report to the Commissioner on the services provided to individuals by the system. (f) Funding (1) Allocation of payments Payments under this section shall be made from amounts made available for the administration of title II and amounts made available for the administration of title XVI, and shall be allocated among those amounts as appropriate. (2) Carryover Any amounts allotted for payment to a protection and advocacy system under this section for a fiscal year shall remain available for payment to or on behalf of the protection and advocacy system until the end of the succeeding fiscal year. (g) Definitions In this section: (1) Beneficiary with a disability The term beneficiary with a disability means an individual who\u2014 (A) is a title II disability beneficiary or a title XVI disability beneficiary (as such terms are defined under section 1148(k)); (B) is an applicant or prospective applicant for benefits under title II or title XVI on the basis that such individual has a disability; (C) is requesting a hearing under section 221(d) or for an administrative review prior to such hearing; or (D) is filing a request for reinstatement of entitled under section 223(i)(1)(A). (2) Commissioner The term Commissioner means the Commissioner of Social Security. (3) Protection and advocacy system The term protection and advocacy system means a protection and advocacy system established pursuant to part C of title I of the Developmental Disabilities Assistance and Bill of Rights Act. (h) Authorization of appropriations There are authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2026 through 2030. .\n#### 12. Social Security assistance and representation grants\n##### (a) In general\nFor each fiscal year during the 5-year period beginning with fiscal year 2026, the Commissioner shall award not less than 10 grants under this section to community-based organizations for the purpose of assisting individuals with disabilities\u2014\n**(1)**\nduring the process of applying for benefits under title II or XVI of the Social Security Act ( 42 U.S.C. 401 et seq. , 1381 et seq.) on the basis of a disability;\n**(2)**\nany appeals processes before the Commissioner, an administrative judge of the Social Security Administration, or a State Disability Determination Services office; and\n**(3)**\nin accessing such benefits.\n##### (b) Grant requirements\n**(1) Duration and amount of grants**\nA grant awarded to a community-based organization under this section\u2014\n**(A)**\nshall be for an amount that is not less than $500,000; and\n**(B)**\nshall be for a period of 5 years.\n**(2) Use of funds**\nGrant funds shall only be used for a purpose described in subsection (a).\n##### (c) Application\n**(1) In general**\nTo receive a grant under this section, a community-based organization shall submit an application to the Commissioner, at such time and in such form and manner and accompanied by such information and assurances as the Commissioner may require.\n**(2) Required information**\nAn application for a grant under this section shall include the following information:\n**(A)**\nThe region to be served by the applicant.\n**(B)**\nA description of the needs of beneficiaries with a disability in such region.\n**(C)**\nA description of services to be provided under such grant.\n**(D)**\nThe personnel that would provide such services.\n**(E)**\nThe applicant's plan for disseminating awareness of the services provided under the grant to beneficiaries with a disability in the region.\n**(3) Memorandum of understanding**\nAn application for a grant under this section shall include a memorandum of understanding among any collaborating entities as to roles and allocation of grant funds for each collaborating agency.\n**(4) Assurance of availability**\nAn application for a grant under this section shall include a commitment by the applicant that all services provided under the grant, including information about such services, shall be accessible to beneficiaries with a disability.\n##### (d) Definitions\n**(1) Beneficiary with a disability**\nThe term beneficiary with a disability has the meaning given such term in section 1150D of the Social Security Act (as added by section 14).\n**(2) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(3) Community-based organization**\nThe term community-based organization means a non-profit agency or collaboration of non-profit agencies that\u2014\n**(A)**\nserves a region of one or more States;\n**(B)**\nincludes\u2014\n**(i)**\na legal team of lawyers licensed to practice in the State or States served by the organization;\n**(ii)**\nexperts in disability benefits provided under title II and XVI of the Social Security Act ( 42 U.S.C. 401 et seq. , 1381 et seq.), including application, and appeals procedures under such titles; and\n**(iii)**\nindividuals currently receiving benefits on the basis of a disability under such a title, or who were beneficiaries under such a title on the basis of a disability within the past 5 years; and\n**(C)**\nis overseen by a board or advisory group composed of at least 1/3 members who are current or former beneficiaries on the basis of a disability under title II or XVI of the Social Security Act.\n**(4) State**\nThe term State means the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n##### (e) Appropriation\nThere is appropriated to the Commissioner, for each of fiscal years 2026 through 2030, $15,000,000 for the purpose of carrying out this section.\n##### (f) Reports\n**(1) In general**\nEach community-based organization that receives a grant under this sections shall provide the Commissioner with\u2014\n**(A)**\nfor each year of the grant period, an annual report on the services provided; and\n**(B)**\nat the conclusion of the grant period, a final report of activities provided under the grant.\n**(2) Evaluation grant**\nFrom the administrative funds of title II and title XVI, there shall be awarded an evaluation grant to an independent entity to evaluate the impact of the grants under this section. The amount to be awarded to the evaluation entity shall be at least $500,000 for each of the 5 years of the grant period and at least $500,000 for the 2 years following the grant period.",
      "versionDate": "2025-09-10",
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
        "name": "Social Welfare",
        "updateDate": "2025-09-23T15:40:34Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2763is.xml"
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
      "title": "Keep Billionaires Out of Social Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T10:58:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Billionaires Out of Social Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-17T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title II of the Social Security Act to permanently appropriate funding for the administrative expenses of the Social Security Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T02:48:25Z"
    }
  ]
}
```
