# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/382
- Title: Dismantle DEI Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 382
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-02-04T05:06:19Z
- Update date including text: 2026-02-04T05:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/382",
    "number": "382",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Dismantle DEI Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T05:06:19Z",
    "updateDateIncludingText": "2026-02-04T05:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:41:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OK"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "KS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WY"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ID"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ND"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "UT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ID"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MO"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s382is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 382\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Schmitt (for himself, Mr. Cotton , Mr. Lankford , Mr. Daines , Mr. Tuberville , Mrs. Blackburn , Mr. Marshall , Ms. Lummis , Mr. Cassidy , Mr. Risch , Mr. Cramer , Mr. Banks , Mr. Sheehy , Mrs. Hyde-Smith , Mr. Scott of Florida , Mr. Lee , Mr. Crapo , Mr. Johnson , Mr. Hawley , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo ensure equal protection of the law, to prevent racism in the Federal Government, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dismantle DEI Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Prohibited diversity, equity, or inclusion practice defined.\nTITLE I\u2014Federal Offices and Personnel\nSec. 101. Executive orders and memoranda rescinded.\nSec. 102. Office of Personnel Management.\nSec. 103. Office of Management and Budget.\nSec. 104. Prohibited use of funds.\nSec. 105. DEI offices closed.\nSec. 106. Prohibited personnel practices.\nTITLE II\u2014Federal Training\nSec. 201. Government-wide training.\nSec. 202. Use of funds.\nTITLE III\u2014Federal Contracting\nSec. 301. Required contract terms.\nSec. 302. Prohibition on discrimination.\nSec. 303. Prohibited use of funds.\nTITLE IV\u2014Federal Grants and Cooperative Agreements\nSec. 401. Required grant agreement terms.\nSec. 402. Required cooperative agreement terms.\nTITLE V\u2014Federal Advisory Committees\nSec. 501. Prohibited diversity, equity, and inclusion practices.\nSec. 502. Administrator responsibilities.\nSec. 503. Agency head responsibilities.\nTITLE VI\u2014Education\nSec. 601. Standards for accreditation of accrediting agencies and associations.\nSec. 602. Prohibited use of funds by the Secretary of Education.\nTITLE VII\u2014Other Matters\nSec. 701. Fannie Mae, Freddie Mac, Federal Home Loan Banks, and Federal Housing Finance Agency.\nSec. 702. Capital markets regulation; corporate boards; self-regulatory organizations.\nSec. 703. Health and Human Services.\nSec. 704. Repeal of diversity, equity, and inclusion programs of Department of Defense.\nSec. 705. Department of Homeland Security and Coast Guard.\nSec. 706. Director of National Intelligence.\nTITLE VIII\u2014Enforcement; severability\nSec. 801. Enforcement; private cause of action.\nSec. 802. Severability.\n#### 3. Prohibited diversity, equity or inclusion practice defined\nThe Civil Rights Act of 1964 ( 42 U.S.C. 2000a et seq. ) is amended by adding at the end the following:\nXII Prohibited diversity, equity or inclusion practice defined 1201. Prohibited diversity, equity, or inclusion practice For purposes of references to this section, the term prohibited diversity, equity, or inclusion practice means\u2014 (1) discriminating for or against any person on the basis of race, color, ethnicity, religion, biological sex, or national origin; (2) requiring as a condition of employment, as a condition for promotion or advancement, or as a condition for speaking, making a presentation, or submitting written materials, that an employee undergo training, education, or coursework, or other pedagogy, that asserts that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; or (3) requiring as a condition of employment, as a condition for promotion or advancement, or as a condition for speaking, making a presentation, or submitting written materials, the signing of or assent to a statement, code of conduct, work program, or plan, or similar device that requires assent by the employee that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. .\nI\nFederal Offices and Personnel\n#### 101. Executive orders and memoranda rescinded\n##### (a) Rescinded Executive Orders and memoranda\n**(1) In general**\nWith respect to an Executive order or memoranda described in paragraph (2), the Executive order or memoranda\u2014\n**(A)**\nshall not have any legal effect; and\n**(B)**\nis revoked in its entirety; and\n**(2) Executive orders and memoranda described**\nThe Executive orders and memoranda described in this paragraph are the following:\n**(A)**\nExecutive Order 13985 ( 5 U.S.C. 601 note; relating to advancing racial equity and support for underserved communities through the Federal Government).\n**(B)**\nExecutive Order 13988 ( 42 U.S.C. 2000e note; relating to preventing and combating discrimination on the basis of gender identity or sexual orientation).\n**(C)**\nExecutive Order 14020, ( 42 U.S.C. 2000e note; relating to the establishment of the White House Gender Policy Council).\n**(D)**\nExecutive Order 14031 ( 42 U.S.C. 3501 note; relating to advancing equity, justice, and opportunity for Asian Americans, Native Hawaiians, and Pacific Islanders).\n**(E)**\nExecutive Order 14035 ( 42 U.S.C. 2000e note; relating to diversity, equity, inclusion, and accessibility in the Federal workforce).\n**(F)**\nExecutive Order 14091 ( 5 U.S.C. 601 note; relating to further advancing racial equity and support for underserved communities through the Federal Government).\n**(G)**\nThe National Security Memorandum on Revitalizing America\u2019s Foreign Policy and National Security Workforce, Institutions, and Partnerships (NSM\u201303) , dated February 4, 2021.\n**(H)**\nThe National Security Memorandum on Advancing the Human Rights of Lesbian, Gay, Bisexual, Transgender, Queer, and Intersex Persons Around the World (NSM\u201304) , dated February 4, 2021.\n##### (b) Carrying out rescinded executive orders and memoranda\nThe head of an executive agency, as defined in section 105 of title 5, United States Code, may not carry out an Executive order or memorandum described in subsection (a)(2).\n##### (c) Programs and office\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the head of a Federal agency under which any program or office carries out an Executive order or memorandum described in subsection (a)(2) between the date of enactment of this Act and 90 days after the date of enactment of this Act shall close, terminate, and wind up the program or office.\n**(2) No reassignment**\nThe head of a Federal agency that closes, terminates, and winds up a program or office under paragraph (1)\u2014\n**(A)**\nshall undertake an appropriate reduction in force; and\n**(B)**\nmay not transfer, reassign, or redesignate any employee or contractor with a position or function that is eliminated by operation of this subsection.\n#### 102. Office of Personnel Management\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Personnel Management shall\u2014\n**(1)**\nrevise all regulations, policies, procedures, manuals, circulars, courses, training, and guidance of the Office such that all such material is in compliance with and consistent with this Act and the amendments made by this Act;\n**(2)**\nrevise so as to effectively rescind all regulations, policies, procedures, manuals, circulars, courses, training, and guidance of the Office that were promulgated, adopted, or implemented to comply with the Executive orders and memoranda described in section 101(a)(2);\n**(3)**\nterminate, close, and wind up the Office of Diversity, Equity, Inclusion, and Accessibility of the Office of Personnel Management (referred to in this paragraph as ODEIA ) and undertake an appropriate reduction in force with respect to, and not transfer, reassign, or redesignate any, employees or contractors of ODEIA, the positions or functions of whom are eliminated by operation of this Act or the amendments made by this Act; and\n**(4)**\nterminate, close, and wind up the Chief Diversity Officers Executive Council and undertake an appropriate reduction in force with respect to, and not transfer, reassign, or redesignate any, employees or contractors of that Council, the positions or functions of whom are eliminated by operation of this Act or the amendments made by this Act.\n##### (b) Chief Diversity Officers Executive Council charter\nEffective on the date of enactment of this Act, the charter of the Chief Diversity Officers Executive Council is revoked.\n##### (c) Prohibition on racism in Government\nSection 1104 of title 5, United States Code, is amended by adding at the end the following:\n(d) (1) In this subsection, the term prohibited diversity, equity, or inclusion practice has the meaning given the term in section 1201 of the Civil Rights Act of 1964. (2) Racist behavior and racist training in the Government are prohibited, including any of the following: (A) Discriminating for or against any person on the basis of race, color, ethnicity, religion, biological sex, or national origin. (B) Training, education, coursework, or use of other pedagogy, that asserts that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. (C) Maintaining an office, bureau, division, or other organization to further promote or enforce a prohibited diversity, equity, or inclusion practice. (D) Retaining or employing a consultant or advisor to further promote or enforce a prohibited diversity, equity, or inclusion practice. (E) Maintaining a rule, a regulation, a policy, guidance, a guideline, management control, a practice, a requirement, training, education, coursework, or a similar device to further promote or enforce a prohibited diversity, equity, or inclusion practice. (F) Requiring as a condition of employment, as a condition for promotion or advancement, or as a condition for speaking, making a presentation, or submitting written materials, the signing of or assent to a statement, code of conduct, work program, or plan, or similar device that requires assent by the employee that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. (3) The Office shall establish standards that shall\u2014 (A) apply to the activities of the Office or any other agency under authority delegated under subsection (a); (B) prohibit racist behavior and racist training in the Government, as described in paragraph (2) of this subsection; (C) ensure compliance with this subsection; (D) ensure compliance with section 717 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u201316 ); and (E) be in accordance with the merit system principles under section 2301. (4) The Office shall establish and maintain an oversight program to ensure that activities under any authority delegated under subsection (a)\u2014 (A) prohibit racist behavior and racist training in the Government, as described in paragraph (2) of this subsection; (B) ensure compliance with this subsection; (C) ensure compliance with section 717 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u201316 ); and (D) are in accordance with the merit system principles under section 2301. .\n#### 103. Office of Management and Budget\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Management and Budget shall\u2014\n**(1)**\nrevise all regulations, policies, procedures, manuals, circulars, courses, training, and guidance of the Office of Management and Budget to ensure those regulations, policies, procedures, manuals, circulars, courses, training, and guidance are in compliance and consistent with this Act and the amendments made by this Act;\n**(2)**\nrescind all regulations, policies, procedures, manuals, circulars, courses, training, and guidance of the Office of Management and Budget that were promulgated, adopted, or implemented to comply with the Executive orders and memoranda described in section 101(a)(2); and\n**(3)**\nrescind the version of Circular A\u20134 of the Office of Management and Budget adopted on November 9, 2023.\n#### 104. Prohibited use of funds\n##### (a) Agency defined\nIn this chapter, the term agency has the meaning given the term in section 3502 of title 44.\n##### (b) Stopping racism in the Federal Government\n**(1) In general**\nNo Federal funds appropriated or otherwise made available by law shall be used for the purpose of maintaining in any agency an\u2014\n**(A)**\noffice relating to diversity, equity, inclusion, or accessibility; or\n**(B)**\na substantially similar office.\n**(2) Prohibition**\nNo Federal funds appropriated or otherwise made available by law shall be used for the purposes of\u2014\n**(A)**\nmaintaining in any agency the Chief Diversity Officers Executive Council or a substantially similar council;\n**(B)**\nmaintaining or employing in any agency a chief diversity officer or a substantially similar officer;\n**(C)**\nsubject to paragraph (3), developing, implementing, distributing, or publishing in any agency\u2014\n**(i)**\nplans, strategic plan, reports, or surveys relating to diversity, equity, inclusion, and accessibility; and\n**(ii)**\naction plans, reports, or surveys relating to equity or substantially similar plans, reports, or surveys;\n**(D)**\ndeveloping, implementing, or maintaining in any agency an employee resource group or an affinity group based on race, color, ethnicity, religion, national origin, sexual orientation, or gender identity;\n**(E)**\ndeveloping, implementing, or maintaining in any agency an agency equity team or a substantially similar team;\n**(F)**\nmaintaining the White House Environmental Justice Interagency Council or a substantially similar Council;\n**(G)**\nmaintaining the Equitable Data Working Group or substantially similar group;\n**(H)**\ndeveloping, implementing, distributing, publishing, establishing, or purchasing in any agency\u2014\n**(i)**\na training course relating to\u2014\n**(I)**\ndiversity;\n**(II)**\nequity;\n**(III)**\ninclusion;\n**(IV)**\na critical theory relating to race, gender, or otherwise; or\n**(V)**\nintersectionality; or\n**(ii)**\na training course substantiality similar to a training course described in clause (i);\n**(I)**\ndeveloping, implementing, or maintaining in any agency a diversity, equity, inclusion, and accessibility data dashboard or a substantially similar data dashboard;\n**(J)**\nmaintaining within the Office of Personnel Management a council relating to diversity, equity, inclusion, or accessibility; or\n**(K)**\nmaintaining or employing in any agency a position relating to diversity, equity, inclusion, or accessibility.\n**(3) Exception**\nThe prohibition under paragraph (2)(C) shall not apply to a plan, report, or survey required by law.\n**(4) Rule of construction**\nNothing in this section shall be construed to prevent the maintenance and funding of\u2014\n**(A)**\nEqual Employment Opportunity offices as historically organized and operated; or\n**(B)**\nan office enforcing the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or similar programs or offices as historically organized and operated.\n#### 105. DEI offices closed\n##### (a) In general\nNot later than 90 days after date of enactment of this Act, the head of any Federal agency that has an office relating to diversity, equity, inclusion, or accessibility\u2014\n**(1)**\nshall\u2014\n**(A)**\nterminate, close, and wind up that office; and\n**(B)**\nundertake an appropriate reduction in force; and\n**(2)**\nmay not transfer, reassign, or redesignate any employee or contractor with a position or function that is eliminated by operation of this subsection.\n##### (b) Application\nNothing in this section shall be construed to prevent the maintenance and funding of\u2014\n**(1)**\nEqual Employment Opportunity offices as historically organized and operated; or\n**(2)**\nan office enforcing the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or similar programs or offices as historically organized and operated.\n#### 106. Prohibited personnel practices\n##### (a) In general\nSection 2302(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (13)(B), by striking or at the end;\n**(2)**\nin paragraph (14), by striking the period at the end and inserting ; or ; and\n**(3)**\nby inserting after paragraph (14) the following:\n(15) take or fail to take, or threaten to take or fail to take, any personnel action against any employee or applicant for employment because of the failure of the employee or applicant to\u2014 (A) complete training with respect to diversity, equity, or inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; (B) complete training that asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; (C) sign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; (D) sign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device that asserts or requires assent by the employee or applicant that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; (E) take any other action that would require the treatment of any individual advantageously or disadvantageously on the basis of that individual\u2019s race, color, ethnicity, religion, biological sex, or national origin; or (F) limit, segregate, or classify employees or applicants for employment in any way that would deprive or tend to deprive any individual of an employment opportunity, or otherwise adversely affect the status of the individual as an employee, because of the race, color, ethnicity, religion, biological sex, or national origin of the individual. .\n##### (b) Performance appraisal systems\nSection 4302 of title 5, United States Code, is amended by adding at the end the following:\n(e) A performance appraisal system may not adversely evaluate an employee for the failure of the employee to\u2014 (1) complete training with respect to diversity, equity, or inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; (2) complete training that asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; (3) sign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; (4) sign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device that asserts or requires assent by the employee that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; (5) take any other action that would require the treatment of any individual advantageously or disadvantageously on the basis of that individual\u2019s race, color, ethnicity, religion, biological sex, or national origin; or (6) limit, segregate, or classify employees or applicants for employment in any way that would deprive or tend to deprive any individual of an employment opportunity, or otherwise adversely affect the status of the individual as an employee, because of the race, color, ethnicity, religion, biological sex, or national origin of the individual. .\n##### (c) SES performance appraisal systems\nSection 4312 of title 5, United States Code, is amended by adding at the end the following:\n(e) A performance appraisal system may not adversely evaluate a senior executive for the failure of the senior executive to\u2014 (1) complete training with respect to diversity, equity, or inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; (2) complete training that asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; (3) sign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; (4) sign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device that asserts or requires assent by the senior executive that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; (5) take any other action that would require the treatment of any individual advantageously or disadvantageously on the basis of that individual\u2019s race, color, ethnicity, religion, biological sex, or national origin; or (6) limit, segregate, or classify employees or applicants for employment in any way that would deprive or tend to deprive any individual of an employment opportunity, or otherwise adversely affect the status of the individual as an employee, because of the race, color, ethnicity, religion, biological sex, or national origin of the individual. .\nII\nFederal Training\n#### 201. Government-wide training\n##### (a) In general\nSection 4103 of title 5, United States Code, is amended by adding at the end the following:\n(d) No training program or plan may be developed, implemented, distributed, published, established, or purchased under this section\u2014 (1) with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; or (2) that asserts or requires the trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. (e) No employee may be required to complete training under a program or plan established under this section\u2014 (1) with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; or (2) that asserts or requires the trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. .\n##### (b) Regulations\nSection 4118 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (c), by striking This section and inserting Except as provided in subsection (d), this section ; and\n**(2)**\nby adding at the end the following:\n(d) The Office shall, in the regulations prescribed under this section, provide that no training program or plan may be developed, implemented, distributed, published, established, or purchased\u2014 (1) with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; or (2) that asserts or requires the trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. .\n#### 202. Use of funds\nNo funds appropriated or otherwise made available by law shall be used for the purpose of developing, implementing, distributing, publishing or purchasing in any Federal agency a training course\u2014\n**(1)**\nrelating to\u2014\n**(A)**\ndiversity, equity, inclusion, and accessibility;\n**(B)**\na critical theory relating to race, gender, or otherwise; or\n**(C)**\nintersectionality, sexual orientation, or gender identity; or\n**(2)**\nthat asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior, inferior, oppressive, oppressed, privileged, or unprivileged.\nIII\nFederal Contracting\n#### 301. Required contract terms\n##### (a) Contracts exceeding $10,000\nSection 6502 of title 41, United States Code, is amended by adding at the end the following:\n(5) Prohibited diversity, equity, or inclusion practice No part of the contract will be performed, and no materials, supplies, articles, or equipment will be manufactured or fabricated under the contract, in plants, factories, buildings, or surroundings, under working conditions or in a working environment, provided by or under the control or supervision of a contractor or any subcontractor who is subject to, or required to comply with, a prohibited diversity, equity or inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964). .\n##### (b) Contracts in other amounts\nSection 6703 of title 41, United States Code, is amended by adding at the end the following:\n(6) Prohibited diversity, equity, or inclusion practice The contract and bid specification shall contain a provision specifying that no part of the services covered by this chapter may be performed in buildings or surroundings, under working conditions or in a working environment, provided by or under the control or supervision of a contractor or any subcontractor who is subject to, or required to comply with, a prohibited diversity, equity or inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964). .\n#### 302. Prohibition on discrimination\n##### (a) In general\nSection 122 of title 40, United States Code, is amended to read as follows:\n122. Prohibition on discrimination (a) Prohibition (1) Discrimination prohibited With respect to a program or activity carried out or receiving Federal assistance under this subtitle, an individual may not be, based on race, color, biological sex, ethnicity, religion, or national origin\u2014 (A) excluded from participation; (B) denied benefits; or (C) otherwise discriminated against. (2) Prohibited diversity, equity, and inclusion practices With respect to a program or activity carried out or receiving Federal assistance under this subtitle, an individual may not be subject to or required to comply with a prohibited diversity, equity, and inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964). (b) Enforcement (1) In general The heads of Federal agencies shall enforce subsection (a) through rules, regulations, policies, and other executive actions of the agency that are similar to rules, regulations, policies, and other executive actions established with respect to racial and other discrimination under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ). (2) Rule of construction Any enforcement under paragraph (1) shall not be construed to bar an individual from pursuing any other legal remedy available to the individual as a result of an action constituting a violation of subsection (a). .\n##### (b) Clerical amendment\nThe table of sections for title 40, United States Code, is amended by striking the item relating to section 122 and inserting the following:\n122. Prohibition on discrimination. .\n#### 303. Prohibited use of funds\n##### (a) Prohibition\nNo funds appropriated or otherwise made available by Federal law may be used by a Federal contractor for purpose of\u2014\n**(1)**\nmaintaining an office relating to diversity, equity, inclusion, or accessibility or a substantially similar office;\n**(2)**\nmaintaining or employing a chief diversity officer or a substantially similar officer; or\n**(3)**\ndeveloping, implementing, distributing, publishing or purchasing\u2014\n**(A)**\na training course relating to\u2014\n**(i)**\ndiversity, equity, inclusion, or accessibility;\n**(ii)**\na critical theory relating to race, gender, or otherwise;\n**(iii)**\nintersectionality; or\n**(iv)**\nsexual orientation or gender identity;\n**(B)**\na training course that is substantially similar to a training course described in subparagraph (A); or\n**(C)**\na training course that asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior, inferior, oppressive, oppressed, privileged, or unprivileged.\n##### (b) Rule of construction\nNothing in this section shall be construed to prevent\u2014\n**(1)**\nthe maintenance and funding of an Equal Employment Opportunity office, as historically organized and operated;\n**(2)**\nan office enforcing the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or similar programs or offices as historically organized and operated; or\n**(3)**\na Federal contractor from using non-Federal funds as the Federal contractor so determines.\nIV\nFederal Grants and Cooperative Agreements\n#### 401. Required grant agreement terms\n##### (a) In general\nChapter 63 of title 31, United States Code, is amended by adding at the end the following:\n6310. Grants and grant agreements (a) Grant Agreement Required Terms The head of an executive agency may not provide a grant to any recipient unless the head of the executive agency and the recipient enter into a grant agreement that contains a provision specifying that no funds appropriated or otherwise made available by Federal law shall be used by the grant recipient for purpose of\u2014 (1) maintaining an office relating to diversity, equity, inclusion, or accessibility; (2) maintaining or employing a chief diversity officer or a substantially similar officer; (3) developing, implementing, distributing, publishing, or purchasing\u2014 (A) a training course relating to\u2014 (i) diversity, equity, inclusion, or accessibility; (ii) a critical theory relating to race, gender, or otherwise; (iii) intersectionality; or (iv) sexual orientation or gender identity; (B) a training course substantially similar to the training courses described in subparagraph (A); or (C) a training course that asserts or requires trainees to assert that a particular race, color, religion, ethnicity, biological sex, or national origin is inherently or systemically superior, inferior, oppressive, oppressed, privileged or unprivileged; or (4) engaging in a prohibited diversity, equity, or inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964). (b) Equal Employment Opportunity Offices Nothing in this section shall be construed to prevent\u2014 (1) the maintenance and funding of an Equal Employment Opportunity office, as historically organized and operated; (2) an office enforcing the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or similar programs or offices as historically organized and operated; or (3) a recipient of a grant from an executive agency from using non-Federal funds as the recipient so determines. (c) Application to HBCUs Nothing in this section shall be construed to prevent the maintenance and funding of Historically Black Colleges and Universities. .\n##### (b) Clerical amendment\nThe table of sections for chapter 63 of title 31, United States Code is amended by adding at the end the following:\n6310. Grants and grant agreements. .\n#### 402. Required cooperative agreement terms\n##### (a) In general\nChapter 63 of title 31, United States Code, as amended by section 401(a), is further amended by adding at the end the following:\n6311. Cooperative agreements (a) Cooperative Agreement Required Terms The head of an executive agency may not enter into a cooperative agreement with a party unless the cooperative agreement contains a provision specifying that no funds appropriated or otherwise made available by Federal law shall be used by any party to the cooperative agreement for purpose of\u2014 (1) maintaining an office relating to diversity, equity, inclusion, or accessibility; (2) maintaining or employing a chief diversity officer or a substantially similar officer; (3) developing, implementing, distributing, publishing, or purchasing\u2014 (A) a training course relating to\u2014 (i) diversity, equity, inclusion, or accessibility; (ii) a critical theory relating to race, gender, or otherwise; (iii) intersectionality; or (iv) sexual orientation or gender identity; (B) a training course substantially similar to the training courses described in subparagraph (A); or (C) a training course that asserts or requires trainees to assert that a particular race, color, religion, ethnicity, biological sex, or national origin is inherently or systemically superior, inferior, oppressive, oppressed, privileged or unprivileged; or (4) engaging in a prohibited diversity, equity, or inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964.). (b) Equal Employment Opportunity Offices Nothing in this section shall be construed to\u2014 (1) prevent the maintenance and funding of an Equal Employment Opportunity office, as historically organized and operated; (2) an office enforcing the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or similar programs or offices as historically organized and operated; or (3) prevent a party to an cooperative agreement with an executive agency from using non-Federal funds as the party so determines. .\n##### (b) Clerical amendment\nThe table of sections for chapter 63 of title 31, United States Code, as amended by section 401(b), is further amended by adding at the end the following:\n6311. Cooperative agreements. .\nV\nFederal Advisory Committees\n#### 501. Prohibited diversity, equity, and inclusion practices\n##### (a) In general\nChapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), is amended by adding at the end the following:\n1015. Diversity, equity, and inclusion practices (a) Prohibited diversity, equity, and inclusion practice defined In this section, the term prohibited diversity, equity, or inclusion practice has the meaning given that term in section 1201 of the Civil Rights Act of 1964. (b) Prohibition The following may not authorize, permit, or implement a prohibited diversity, equity, or inclusion practice with respect to any advisory committee established by the head of an agency: (1) The Administrator. (2) The agency head. (3) The chair of the advisory committee. (4) The advisory committee. (c) Termination of committee (1) Finding by Administrator With respect to an advisory committee, if the Administrator finds that the applicable agency head, the chair of the advisory committee, or the advisory committee authorized, permitted, or implemented a prohibited diversity, equity, or inclusion practice, then the advisory committee shall terminate not later than 30 days after the Administrator makes such finding. (2) Finding by Inspector General With respect to an advisory committee, if the Inspector General for the agency that established the advisory committee finds that the applicable agency head, chair of the advisory committee, or the advisory committee authorized, permitted, or implemented a prohibited diversity, equity, or inclusion practice, then the advisory committee shall terminate not later than 30 days after the Inspector General makes such finding. (d) Action (1) In general Any person may bring an action in any United States district court seeking a determination that the Administrator, any agency head, any chair of an advisory committee, or any advisory committee authorized, permitted, or implemented a prohibited diversity, equity, or inclusion practice with respect to an advisory committee. (2) Order directing termination of advisory committee If after an evidentiary hearing, a court determines that the defendant authorized, permitted, or implemented a prohibited diversity, equity, or inclusion practice, the court shall issue an order directing the Administrator to immediately terminate that advisory committee. (3) Additional awards In an action brought under this subsection in which the plaintiff prevails, the court may award\u2014 (A) a Writ of Mandamus or other equitable or declaratory relief; (B) a minimum of $1,000 per violation per day; (C) reasonable attorney\u2019s fees and litigation costs; (D) compensatory damages; and (E) all other appropriate relief. .\n##### (b) Clerical amendment\nThe table of sections for chapter 10 of title 5, United States Code, is amended by inserting after the item relating to section 1014 the following:\n1015. Diversity, equity, and inclusion practices. .\n#### 502. Administrator responsibilities\n##### (a) Compliance\nSubsection (b)(1) of section 1006 of title 5, United States Code, is amended\u2014\n**(1)**\nin subparagraph (C), by striking the word or at the end;\n**(2)**\nin subparagraph (D), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(E) whether the committee is in compliance with the Dismantle DEI Act of 2025 . .\n##### (b) Guidelines and management controls\nSection 1006 of title 5, United States Code, is further amended by adding at the end the following:\n(f) Guidelines and management controls related to the End Racism in Federal Advisory Committees Act The Administrator shall\u2014 (1) prescribe administrative guidelines and management controls applicable to advisory committees to enforce the requirements of the Dismantle DEI Act of 2025 ; and (2) ensure that the Committee Management Secretariat complies with and enforces the requirements of the Dismantle DEI Act of 2025 . .\n##### (c) Revised rules, regulations and guidance\nNot later than 180 days after the date of enactment of this Act, the Administrator shall ensure that all rules, regulations, policies, guidance, guidelines, management controls, governing documents, practices, requirements, training, education, coursework, or similar devices are revised to the extent that they are inconsistent with this Act.\n#### 503. Agency head responsibilities\n##### (a) Agency head responsibilities\nSubsection (a) of section 1007 of title 5, United States Code, is amended by adding at the end the following: Each agency head shall establish uniform administrative guidelines and management controls to ensure compliance with the Dismantle DEI Act of 2025 . .\n##### (b) Compliance\nSubsection (b) of section 1007 of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) ensure compliance with the Dismantle DEI Act of 2025 . .\nVI\nEducation\n#### 601. Standards for accreditation of accrediting agencies and associations\nSection 496(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1099b(c) ) is amended\u2014\n**(1)**\nin paragraph (8), by striking and at the end;\n**(2)**\nin paragraph (9), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(10) confirms that the standards for accreditation of the agency or association do not\u2014 (A) require, encourage, or coerce any institution of higher education to engage in prohibited diversity, equity, and inclusion practices (as defined in section 1201 of the Civil Rights Act of 1964); (B) assess the commitment of an institution of higher education to any ideology, belief, or viewpoint; (C) prohibit or discourage an institution of higher education from engaging in activity protected by the Constitution, including having a religious mission, operating as a religious institution, or being controlled by or associated with a religious organization; or (D) discriminate against an institution of higher education for engaging in religious speech, religious practice, or religious exercise. .\n#### 602. Prohibited use of funds by the Secretary of Education\nSection 8527 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7907 ) is amended by adding at the end the following:\n(e) Prohibition; Rules of Construction (1) Prohibition None of the funds provided to the Secretary of Education under this Act may be used by the Secretary, including through a grant, contract, or cooperative agreement, to\u2014 (A) maintain an Office of Diversity, Equity, Inclusion, and Accessibility, an Office of Diversity, Equity, and Inclusion, an Office of Diversity and Inclusion, a Diversity Office or a substantially similar office; (B) maintain or employ a Chief Diversity Officer or substantially similar officer; (C) develop, implement, distribute, publish, or purchase a training course or substantially similar course relating to any of the following\u2014 (i) diversity, equity, inclusion, and accessibility (DEIA); (ii) diversity, equity, and inclusion; (iii) diversity and inclusion; (iv) diversity; (v) critical theory (race, gender, or otherwise); (vi) intersectionality; or (vii) sexual orientation or gender identity; or (D) develop, implement, distribute, publish, or purchase a training course or substantially similar course that asserts or requires trainees to assert that a particular race, color ethnicity, religion, biological sex, or national origin is inherently or systemically superior, inferior, oppressive or oppressed, privileged or unprivileged. (2) Rules of construction Nothing in this section shall be construed to\u2014 (A) prohibit the maintenance and funding of Equal Employment Opportunity offices or officers, as historically organized and operated; (B) prohibit the maintenance and funding of offices enforcing the Americans with Disabilities Act of 1990 or similar programs or offices, as historically organized and operated; or (C) impact the use of non-Federal funds by a contractor of the Department of Education or by a grant recipient of funds from the Secretary of Education. .\nVII\nOther Matters\n#### 701. Fannie Mae, Freddie Mac, Federal Home Loan Banks, and Federal Housing Finance Agency\nSection 1319A of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4520 ) is repealed.\n#### 702. Capital markets regulation; corporate boards; self-regulatory organizations\n##### (a) Repeal of Offices of Minority and Women Inclusion\n**(1) In general**\nSection 342 of the Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5452 ) is repealed.\n**(2) Technical and conforming amendments**\n**(A) Consumer Financial Protection Act of 2010**\nSection 1016(c) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5496(c) ) is amended\u2014\n**(i)**\nin paragraph (7), by adding and at the end;\n**(ii)**\nin paragraph (8), by striking ; and and inserting a period; and\n**(iii)**\nby striking paragraph (9).\n**(B) Dodd-Frank Wall Street Reform and Consumer Protection Act**\nThe table of contents for the Dodd-Frank Wall Street Reform and Consumer Protection Act is amended by striking the item relating to section 342.\n##### (b) Boards of public companies subject to civil rights act\nSection 701 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e ) is amended by adding at the end of subsection (f) the following: The term employee includes any person who serves on a board of directors of an issuer that has a registration statement in effect as to a security under the Securities Act of 1933 and is compensated by the issuer. .\n##### (c) Prohibition on racism\n**(1) In general**\nThe Gramm-Leach-Bliley Act ( Public Law 106\u2013102 ) is amended by inserting after section 503 ( 15 U.S.C. 6803 ) the following:\n503A. Prohibited diversity, equity and inclusion practices No Federal functional regulator shall engage in a prohibited diversity, equity, and inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964) or require (whether by regulation, enforcement action, guidance, examination or otherwise) that any person regulated by the Federal functional regulator engage in a prohibited diversity, equity, and inclusion practice. .\n**(2) Clerical amendment**\nThe table of contents for the Gramm-Leach-Bliley Act ( Public Law 106\u2013102 ) is amended by inserting after the item relating to section 503 the following:\nSec. 503A. Prohibited diversity, equity and inclusion practices. .\n##### (d) National securities associations\nSection 15A of the Securities Exchange Act of 1934 ( 15 U.S.C. 78o\u20133 ) is amended by adding at the end the following:\n(o) Prohibited diversity, equity and inclusion practices No national securities association shall engage in a prohibited diversity, equity, and inclusion practice (as defined in section 1201 of the Civil Rights Act of 1964) or require (whether by rule, enforcement action, guidance, examination, or otherwise) that any member of the national securities association engage in a prohibited diversity, equity, and inclusion practice. .\n##### (e) Community Development Advisory Board member requirements\nSection 104(d)(2)(G) of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4703(d)(2)(G) ) is amended, in the matter preceding clause (i), by striking and racial, ethnic, and gender diversity .\n#### 703. Health and Human Services\nSection 821 of the Public Health Service Act ( 42 U.S.C. 296m ) is repealed.\n#### 704. Repeal of diversity, equity, and inclusion programs of Department of Defense\n##### (a) Repeal of reporting requirements on diversity and inclusion\nSection 113 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby striking paragraph (2); and\n**(B)**\nby redesignating paragraphs (3) and (4) as paragraphs (2) and (3), respectively;\n**(2)**\nin subsection (g)(1)(B)\u2014\n**(A)**\nby striking clause (vii); and\n**(B)**\nby redesignating clauses (viii), (ix), and (x) as clauses (vii), (viii), and (ix), respectively; and\n**(3)**\nby striking subsections (l) and (m) and by redesignating subsections (n) and (o) as subsections (l) and (m), respectively.\n##### (b) Repeal of Chief Diversity Officer\n**(1) In general**\nSection 147 of title 10, United States Code, is repealed.\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 4 of such title is amended by striking the item relating to section 147.\n##### (c) Repeal of program on diversity in military leadership\n**(1) In general**\nSection 656 of title 10, United States Code, is repealed.\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 37 of such title is amended by striking the item relating to section 656.\n#### 705. Department of Homeland Security and Coast Guard\n##### (a) In general\nParagraph (3) of section 845(c) of the Homeland Security Act of 2002 ( 6 U.S.C. 415(c) ) is repealed.\n##### (b) Coast Guard\nSection 1903(d)(2) of title 14, United States Code, is amended by striking , including diversity, inclusion, and issues regarding women specifically .\n#### 706. Director of National Intelligence\nSection 5704 of the Damon Paul Nelson and Matthew Young Pollard Intelligence Authorization Act for Fiscal Years 2018, 2019, and 2020 ( 50 U.S.C. 3334b ) is repealed.\nVIII\nEnforcement; severability\n#### 801. Enforcement; private cause of action\n##### (a) Enforcement\nAny person alleging a violation of this Act may bring a civil action in any United States District Court.\n##### (b) Relief\nIn a civil action brought under subsection (a) in which the plaintiff prevails, the court may award\u2014\n**(1)**\na Writ of Mandamus or other equitable or declaratory relief;\n**(2)**\na minimum of $1,000 per violation per day;\n**(3)**\nreasonable attorney\u2019s fees and litigation costs;\n**(4)**\ncompensatory damages; and\n**(5)**\nall other appropriate relief.\n#### 802. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of such provision or amendment to any person or circumstance shall not be affected thereby.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committees on the Judiciary, Education and Workforce, Armed Services, Foreign Affairs, Financial Services, Energy and Commerce, Transportation and Infrastructure, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "925",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dismantle DEI Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Coast guard",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Department of Defense",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Director of National Intelligence",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Employee performance",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Government corporations and government-sponsored enterprises",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Military command and structure",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Minority employment",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-04-11T18:23:37Z"
          },
          {
            "name": "Office of Personnel Management (OPM)",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-04-11T18:23:36Z"
          },
          {
            "name": "Women's employment",
            "updateDate": "2025-04-11T18:23:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-10T17:54:56Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s382is.xml"
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
      "title": "Dismantle DEI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dismantle DEI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure equal protection of the law, to prevent racism in the Federal Government, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:33Z"
    }
  ]
}
```
