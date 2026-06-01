# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1354
- Title: Justice for All Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1354
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-04-29T17:04:43Z
- Update date including text: 2026-04-29T17:04:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1354",
    "number": "1354",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Justice for All Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T17:04:43Z",
    "updateDateIncludingText": "2026-04-29T17:04:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-13T14:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MO"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "GA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "DC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MD"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "TX"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "LA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1354ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1354\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Ms. Tlaib (for herself, Mr. Cleaver , Ms. Lee of Pennsylvania , Mr. Johnson of Georgia , Mr. Garc\u00eda of Illinois , Ms. Norton , Ms. Kamlager-Dove , Mrs. McIver , Mr. Frost , Ms. Adams , Ms. Pressley , Mr. Jackson of Illinois , Mrs. Ramirez , and Mr. Mfume ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Civil Rights Act of 1964 to clarify that disparate impacts on certain populations constitute a sufficient basis for rights of action under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for All Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThis Act is made necessary by a decision of the Supreme Court in Alexander v. Sandoval, 532 U.S. 275 (2001) that significantly impairs statutory protections against discrimination that Congress has erected over a period of almost 4 decades. The Sandoval decision undermines these statutory protections by stripping victims of discrimination (defined under regulations that Congress required Federal departments and agencies to promulgate to implement title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. )) of the right to bring action in Federal court to redress the discrimination.\n**(2)**\nThe Sandoval decision contradicts settled expectations created by title VI of the Civil Rights Act of 1964 , title IX of the Education Amendments of 1972 (also known as the Patsy Takemoto Mink Equal Opportunity in Education Act ) ( 20 U.S.C. 1681 et seq. ), the Age Discrimination Act of 1975 ( 42 U.S.C. 6101 et seq. ), and section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) (collectively referred to in this Act as the covered civil rights provisions ). The covered civil rights provisions were designed to establish and make effective the rights of persons to be free from discrimination on the part of entities that are subject to 1 or more of the covered civil rights provisions, as appropriate (referred to in this Act as covered entities ). In 1964 Congress adopted title VI of the Civil Rights Act of 1964 to ensure that Federal dollars would not be used to subsidize or support programs or activities that discriminated on racial, color, or national origin grounds. In the years that followed, Congress extended these protections by enacting laws barring discrimination in federally funded education activities on the basis of sex in title IX of the Education Amendments of 1972, and discrimination in federally funded activities on the basis of age in the Age Discrimination Act of 1975 and disability in section 504 of the Rehabilitation Act of 1973 .\n**(3)**\nAll of the statutes cited in this section were designed to protect persons subject to discrimination. As Congress has consistently recognized, effective enforcement of the statutes and protection of the rights guaranteed under the statutes depend heavily on the efforts of private attorneys general. Congress acknowledged that it could not secure compliance solely through administrative efforts and enforcement actions initiated by the Attorney General. Newman v. Piggie Park Enterprises, 390 U.S. 400 (1968) (per curiam).\n**(4)**\nThe Supreme Court has made it clear that individuals suffering discrimination under these statutes have a private right of action in the Federal courts, and that this is necessary for effective protection of the law, although Congress did not make such a right of action explicit in the statute involved. Cannon v. University of Chicago, 441 U.S. 677 (1979).\n**(5)**\nFurthermore, for effective enforcement of the statutes cited in this section, it is necessary that the private right of action include a means to challenge all forms of discrimination that are prohibited by the statutes, including practices that have a disparate impact and are not justified as necessary to achieve the legitimate goals of programs or activities supported by Federal financial assistance.\n**(6)**\nBy reinstating a private right of action to challenge disparate impact discrimination under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) and confirming that right for other civil rights statutes, Congress is not acting in a manner that would expose covered entities to unfair findings of discrimination. The legal standard for a disparate impact claim has never been structured so that a finding of discrimination could be based on numerical imbalance alone.\n**(7)**\nIn contrast, a failure to reinstate or confirm a private right of action would leave vindication of the rights to equality of opportunity solely to Federal agencies. Action by Congress to specify a private right of action is necessary to ensure that persons will have a remedy if they are denied equal access to education, housing, health, environmental protection, transportation, and many other programs and services by practices of covered entities that result in discrimination.\n**(8)**\nAs a result of the Supreme Court\u2019s decision in Sandoval, courts have dismissed numerous claims brought under the regulations promulgated pursuant to title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) that challenged actions with an unjustified discriminatory effect. Although the Sandoval Court did not address title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), lower courts have similarly dismissed claims under such title.\n**(9)**\nSection 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) has received different treatment by the Supreme Court. In Alexander v. Choate, 469 U.S. 287 (1985), the Court proceeded on the assumption that the statute itself prohibited some actions that had a disparate impact on disabled individuals\u2014an assumption borne out by congressional statements made during passage of the Act. In Sandoval, the Court appeared to accept this principle of Alexander. Moreover, the Supreme Court explicitly recognized congressional approval of the regulations promulgated to implement section 504 of the Rehabilitation Act of 1973 in Consolidated Rail Corp. v. Darrone, 465 U.S. 624, 634 (1984). Relying on the validity of the regulations, Congress incorporated the regulations into the statutory requirements of section 204 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12134 ). Nonetheless, Sandoval creates the potential for uncertainty in the application of critical protections of Section 504, particularly in the lower courts.\n**(10)**\nThe right to maintain a private right of action under a provision added to a statute under this Act will be effectuated by a waiver of sovereign immunity in the same manner as sovereign immunity is waived under the remaining provisions of that statute.\n**(11)**\nNumerous provisions of Federal law expressly prohibit discrimination on the basis of sex, and Federal agencies and courts have correctly interpreted these prohibitions on sex discrimination to include discrimination based on sexual orientation, gender identity, and sex stereotypes. In particular, the Equal Employment Opportunity Commission correctly interpreted title VII of the Civil Rights Act of 1964 in Macy v. Holder, Baldwin v. Foxx, and Lusardi v. McHugh.\n**(12)**\nIn forbidding discrimination based on sex, Congress intended to strike at the entire spectrum of disparate treatment resulting from sex-related characteristics. The Supreme Court correctly recognized in Price Waterhouse v. Hopkins and Oncale v. Sundowner Offshore Services that among these characteristics are sex-stereotypes, including masculinity and femininity. Congress reaffirmed in the Pregnancy Discrimination Act of 1978 that discrimination on the basis of sex includes but is not limited to discrimination on the basis of pregnancy, childbirth, or related medical conditions. .\n**(13)**\nThe absence of explicit prohibitions of discrimination on the basis of sexual orientation and gender identity under Federal statutory law has created uncertainty for employers and other entities covered by Federal nondiscrimination laws and caused unnecessary hardships for LGBTQ individuals.\n**(14)**\nThe Supreme Court correctly recognized in Hobby Lobby v. Burwell that the Religious Freedom Restoration Act of 1993 (RFRA) provides no \u2026 shield to those who cloak discrimination as religious practice to escape legal sanction. This Act reaffirms that crucial limitation on RFRA, that Congress did not intend for it to be used\u2014and indeed it cannot be used\u2014to provide a defense against allegations of discrimination on the basis of any protected trait.\n**(15)**\nChapter 1 of title 9, United States Code (commonly known as the Federal Arbitration Act ), represented an exercise of legislative power that required courts to recognize private voluntary agreements to arbitrate commercial disputes at a time when the courts were refusing to do so on grounds that arbitration represented a usurpation of the authority of the courts to resolve legal disputes.\n**(16)**\nThe Federal Arbitration Act did not, and should not have been interpreted to, supplant or nullify the legislatively created rights and remedies that Congress, exercising its power under article I of the Constitution of the United States, has granted to the people of the United States for resolving disputes in State and Federal courts.\n**(17)**\nRecent court decisions, including AT&T Mobility LLC v. Concepcion, 563 U.S. 333 (2011) and American Express Co. v. Italian Colors Restaurant, 133 S. Ct. 2304 (2013), have interpreted the Federal Arbitration Act to broadly preempt rights and remedies established under substantive State and Federal law. As a result, these decisions have enabled business entities to avoid or nullify legal duties created by congressional enactment, resulting in millions of people in the United States being unable to vindicate their rights in State and Federal courts.\n**(18)**\nStates have a compelling interest in enacting rights and remedies to protect the welfare of their citizens, and the Federal Arbitration Act should not be, and should not have been, interpreted to preempt State legislation that enacted rights and remedies to protect the welfare of their citizens.\n**(19)**\nThe Supreme Court misinterpreted title VII of the Civil Rights Act in establishing the Faragher-Ellerth affirmative defense in Faragher v. City of Boca Raton and Burlington Industries, Inc. v. Ellerth. This affirmative defense often leaves victims of sexual harassment with no remedy or recourse after incidence of sexual or other harassment. Violations of the law, and injuries to a victim and their rights, are not cured by the existence of an anti-harassment policy or the lack of future harm, and in a hostile work environment taking preventative measures is not a requirement that falls on the victim.\n**(20)**\nBringing a lawsuit to vindicate civil rights is financially risky, and law firms, whether large or small, are unlikely to take such cases on. Congress enacted the Civil Rights Attorney's Fees Award Act of 1976 in order to make lawsuits to vindicate civil rights more accessible to potential plaintiffs. The Supreme Court correctly recognized in City of Riverside v. Rivera that the effectuation of congressional intent requires viable civil rights lawsuits, which are dependent on the availability of private enforcement mechanisms and the corresponding availability of attorney\u2019s fees.\n**(21)**\nHowever, the Supreme Court incorrectly held that the catalyst theory is not a permissible basis for the award of attorney's fees in Buckhannon v. West Virginia Department of Health & Human Resources. In doing so, the Court deprived plaintiffs who effectively win a lawsuit through a settlement, from receiving pre-trial attorney\u2019s fees. Congress enacted fee-shifting provisions in civil rights laws to encourage private enforcement of those laws, and fees must be awarded when a lawsuit vindicates the rights Congress sought to secure. In disapproving of the \u201ccatalyst theory\u201d the Court incentivized potential defendants to draw out the pre-trial process and settle at the last second, making the lawsuit too expensive for the average victim to undertake and too risky for the average attorney to accept a civil rights case.\n**(22)**\nThe Civil Rights Act of 1964, and other civil rights laws that followed it, were written, in part, to banish rampant disparate treatment on the basis of race from American society. Congress sought to overcome the pervasive, racist ideology that Black traits were inferior by prohibiting discrimination, and intended the Act to be interpreted broadly\u2014encompassing race and all its attributes, especially those traits historically associated with race.\n**(23)**\n\u201cBlackness\u201d and its associated physical traits, such as dark skin and kinky and curly hair, have too often been equated with inferiority and \u201cunprofessionalism.\u201d Professionalism was, and still is, closely linked to European features and mannerisms, which entails that those who do not naturally fall into Eurocentric norms must alter their appearances, sometimes drastically and permanently, in order to be deemed professional. Such norms are, on their face, proxies for race.\n**(24)**\nFederal courts have correctly interpreted, e.g. that title VII of the Civil Rights Act of 1964 prohibits discrimination on the basis of race, and thus protect individuals from discrimination against afros. However, the courts have yet to accept that the Act outlaws dress codes and grooming policies that prohibit any natural presentation of Black hair, including afros, braids, twists, and locks. Although purportedly \u201crace-neutral\u201d, these policies have a disparate impact on Black individuals as they are more likely to deter, burden, or punish Black individuals than any other group. Therefore, hair discrimination targeting hairstyles associated with race is racial discrimination.\n#### 3. Prohibited discrimination\n##### (a) Civil Rights Act of 1964\nSection 601 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d ) is amended\u2014\n**(1)**\nby striking No and inserting (a) No ;\n**(2)**\nby inserting religion, sex (as such term is defined in section 208), before or national origin ; and\n**(3)**\nby adding at the end the following:\n(b) (1) (A) Discrimination (including exclusion from participation and denial of benefits) based on disparate impact is established under this title only if\u2014 (i) a person aggrieved by discrimination on the basis of race, color, sex (as defined in section 208), or national origin (referred to in this title as an person aggrieved demonstrates that an entity subject to this title (referred to in this title as a covered entity ) has a policy or practice that causes a disparate impact on the basis of race, color, sex (as such term is defined in section 208), or national origin and the covered entity fails to demonstrate that the challenged policy or practice is related to and necessary to achieve the nondiscriminatory goals of the program or activity alleged to have been operated in a discriminatory manner; or (ii) the person aggrieved demonstrates (consistent with the demonstration required under title VII with respect to an alternative employment practice ) that a less discriminatory alternative policy or practice exists, and the covered entity refuses to adopt such alternative policy or practice. (B) (i) With respect to demonstrating that a particular policy or practice causes a disparate impact as described in subparagraph (A)(i), the person aggrieved shall demonstrate that each particular challenged policy or practice causes a disparate impact, except that if the person aggrieved demonstrates to the court that the elements of a covered entity\u2019s decisionmaking process are not capable of separation for analysis, the decisionmaking process may be analyzed as 1 policy or practice. (ii) If the covered entity demonstrates that a specific policy or practice does not cause the disparate impact, the covered entity shall not be required to demonstrate that such policy or practice is necessary to achieve the goals of its program or activity. (2) A demonstration that a policy or practice is necessary to achieve the goals of a program or activity may not be used as a defense against a claim of intentional discrimination under this title. (3) In this subsection, the term demonstrates means meets the burdens of production and persuasion. .\n##### (b) Education Amendments of 1972\nSection 901 of the Education Amendments of 1972 ( 20 U.S.C. 1681 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) (1) (A) Subject to the conditions described in paragraphs (1) through (9) of subsection (a), discrimination (including exclusion from participation and denial of benefits) based on disparate impact is established under this title only if\u2014 (i) a person aggrieved by discrimination on the basis of sex (as such term is defined in section 208 of the Civil Rights Act of 1964) (referred to in this title as an person aggrieved ) demonstrates that an entity subject to this title (referred to in this title as a covered entity ) has a policy or practice that causes a disparate impact on the basis of sex and the covered entity fails to demonstrate that the challenged policy or practice is related to and necessary to achieve the nondiscriminatory goals of the program or activity alleged to have been operated in a discriminatory manner; or (ii) the person aggrieved demonstrates (consistent with the demonstration required under title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ) with respect to an alternative employment practice ) that a less discriminatory alternative policy or practice exists, and the covered entity refuses to adopt such alternative policy or practice. (B) (i) With respect to demonstrating that a particular policy or practice causes a disparate impact as described in subparagraph (A)(i), the person aggrieved shall demonstrate that each particular challenged policy or practice causes a disparate impact, except that if the person aggrieved demonstrates to the court that the elements of a covered entity\u2019s decisionmaking process are not capable of separation for analysis, the decisionmaking process may be analyzed as 1 policy or practice. (ii) If the covered entity demonstrates that a specific policy or practice does not cause the disparate impact, the covered entity shall not be required to demonstrate that such policy or practice is necessary to achieve the goals of its program or activity. (2) A demonstration that a policy or practice is necessary to achieve the goals of a program or activity may not be used as a defense against a claim of intentional discrimination under this title. (3) In this subsection, the term demonstrates means meets the burdens of production and persuasion. .\n##### (c) Age Discrimination Act of 1975\nSection 303 of the Age Discrimination Act of 1975 ( 42 U.S.C. 6102 ) is amended\u2014\n**(1)**\nby striking Pursuant and inserting (a) Pursuant ; and\n**(2)**\nby adding at the end the following:\n(b) (1) (A) Subject to the conditions described in subsections (b) and (c) of section 304, discrimination (including exclusion from participation and denial of benefits) based on disparate impact is established under this title only if\u2014 (i) a person aggrieved by discrimination on the basis of age (referred to in this title as a person aggrieved ) demonstrates that an entity subject to this title (referred to in this title as a covered entity ) has a policy or practice that causes a disparate impact on the basis of age and the covered entity fails to demonstrate that the challenged policy or practice is related to and necessary to achieve the nondiscriminatory goals of the program or activity alleged to have been operated in a discriminatory manner; or (ii) the person aggrieved demonstrates (consistent with the demonstration required under title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ) with respect to an alternative employment practice ) that a less discriminatory alternative policy or practice exists, and the covered entity refuses to adopt such alternative policy or practice. (B) (i) With respect to demonstrating that a particular policy or practice causes a disparate impact as described in subparagraph (A)(i), the person aggrieved shall demonstrate that each particular challenged policy or practice causes a disparate impact, except that if the person aggrieved demonstrates to the court that the elements of a covered entity\u2019s decisionmaking process are not capable of separation for analysis, the decisionmaking process may be analyzed as 1 policy or practice. (ii) If the covered entity demonstrates that a specific policy or practice does not cause the disparate impact, the covered entity shall not be required to demonstrate that such policy or practice is necessary to achieve the goals of its program or activity. (2) A demonstration that a policy or practice is necessary to achieve the goals of a program or activity may not be used as a defense against a claim of intentional discrimination under this title. (3) In this subsection, the term demonstrates means meets the burdens of production and persuasion. .\n##### (d) Fair Housing Act\nThe Fair Housing Act (title VIII of the Civil Rights Act of 1968; 42 U.S.C. 3601 et seq. ) is amended\u2014\n**(1)**\nin section 802, by adding at the end the following:\n(p) Sex has the meaning given such term in section 208 of the Civil Rights Act of 1964. (q) Source of income includes\u2014 (1) any income from a profession, occupation, or job; (2) any form of Federal, State, or local housing assistance provided to a family or provided to a housing owner on behalf of a family, or private assistance, grant, loan or rental assistance program, including low-income housing assistance certificates, rental subsidies from nongovernmental organizations, and vouchers issued under the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ); (3) any income received during a taxable year as Social Security benefits, as defined in section 86(d) of the Internal Revenue Code of 1986, or as supplemental security income benefits under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ); (4) any gift, inheritance, pension, annuity, or other consideration or benefit; (5) any income received pursuant to court order, including spousal support and child support; (6) any payment from a trust, guardian, or conservator; (7) any income from the sale or pledge of property or an interest in property; and (8) any other lawful source of income. (r) Race , color , religion , sex , sexual orientation , gender identity , handicap , familial status , source of income , or national origin , used with respect to an individual, includes\u2014 (1) the race, color, religion, sex, sexual orientation, gender identity, handicap, familial status, source of income, or national origin, respectively, of another person with whom the individual is associated or has been associated; and (2) a perception or belief, even if inaccurate, concerning the race, color, religion, sex, sexual orientation, gender identity, handicap, familial status, source of income, or national origin, respectively, of the individual. ;\n**(2)**\nin section 804, by inserting (as defined in section 208 of the Civil Rights Act of 1964), source of income, after sex each place that term appears;\n**(3)**\nin section 805, by inserting (as defined in section 208 of the Civil Rights Act of 1964), source of income, after sex each place that term appears;\n**(4)**\nin section 806, by inserting (as defined in section 208 of the Civil Rights Act of 1964), source of income, after sex ;\n**(5)**\nin section 807 ( 42 U.S.C. 3607 ), by adding at the end the following:\n(c) Nothing in this title shall be construed to\u2014 (1) prohibit an entity from providing housing assistance under section 8(o)(19) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(19) ) in a nondiscriminatory manner; or (2) limit the ability of the owner of a dwelling to determine, in a commercially reasonable and non-discriminatory manner, the ability of a person to afford to purchase or rent the dwelling. ; and\n**(6)**\nin section 808(e)(6) ( 42 U.S.C. 3608(e)(6) ), by inserting source of income, after handicap, .\n##### (e) Prevention of intimidation in Fair Housing cases\nSection 901 of the Civil Rights Act of 1968 ( 42 U.S.C. 3631 ) is amended by inserting (as such term is defined in section 208 of the Civil Rights Act of 1964), source of income (as defined in section 802), after sex each place that term appears.\n#### 4. Right of recovery\n##### (a) Civil Rights Act of 1964\nTitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) is amended by inserting after section 602 the following:\n602A. Actions brought by persons aggrieved (a) Claims Based on Proof of Intentional Discrimination In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful intentional discrimination (not a practice that is unlawful because of its disparate impact) prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (b) Claims Based on the Disparate Impact Standard of Proof In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful discrimination based on disparate impact prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (c) Settlement In any settlement agreement or consent decree to resolve an action brought or which may be brought under this title, attorney\u2019s fees of the plaintiff shall be included. .\n##### (b) Education Amendments of 1972\nTitle IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ) is amended by inserting after section 902 the following:\n902A. Actions brought by persons aggrieved (a) Claims Based on Proof of Intentional Discrimination In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful intentional discrimination (not a practice that is unlawful because of its disparate impact) prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (b) Claims Based on the Disparate Impact Standard of Proof In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful discrimination based on disparate impact prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (c) Settlement In any settlement agreement or consent decree to resolve an action brought or which may be brought under this title, attorney\u2019s fees of the plaintiff shall be included. .\n##### (c) Age Discrimination Act of 1975\n**(1) In general**\nSection 305 of the Age Discrimination Act of 1975 ( 42 U.S.C. 6104 ) is amended by adding at the end the following:\n(g) (1) In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful intentional discrimination (not a practice that is unlawful because of its disparate impact) prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (2) In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful discrimination based on disparate impact prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (3) In any settlement agreement or consent decree to resolve an action brought or which may be brought under this title, attorney\u2019s fees of the plaintiff shall be included. .\n**(2) Conformity of ada with title vi and title ix**\n**(A) Eliminating waiver of right to fees if not requested in complaint**\nSection 305(e)(1) of the Age Discrimination Act of 1975 ( 42 U.S.C. 6104(e) ) is amended\u2014\n**(i)**\nby striking to enjoin a violation and inserting to redress a violation ; and\n**(ii)**\nby striking the second sentence and inserting the following: The Court shall award the costs of suit, including a reasonable attorney\u2019s fee (including expert fees), to the prevailing plaintiff. .\n**(B) Eliminating unnecessary mandates: to exhaust administrative remedies; and to delay suit longer than 180 days to obtain agency review**\nSection 305(f) of the Age Discrimination Act of 1975 ( 42 U.S.C. 6104(f) ) is amended by striking With respect to actions brought for relief based on an alleged violation of the provisions of this title, and inserting Actions brought for relief based on an alleged violation of the provisions of this title may be initiated in a court of competent jurisdiction, pursuant to section 305(e), or before the relevant Federal department or agency. With respect to such actions brought initially before the relevant Federal department or agency, .\n**(C) Eliminating duplicative reasonableness requirement; clarifying that reasonable factors other than age is defense to a disparate impact claim, not an exception to ada coverage**\nSection 304(b)(1) of the Age Discrimination Act of 1975 ( 42 U.S.C. 6103(b)(1) ) is amended by striking involved\u2014 and all that follows through the period and inserting involved such action reasonably takes into account age as a factor necessary to the normal operation or the achievement of any statutory objective of such program or activity. .\n##### (d) Rehabilitation Act of 1973\nSection 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) is amended by adding at the end the following:\n(e) (1) In an action brought by a person aggrieved by discrimination on the basis of disability (referred to in this section as an person aggrieved ) under this section against an entity subject to this section (referred to in this section as a covered entity ) who has engaged in unlawful intentional discrimination (not a practice that is unlawful because of its disparate impact) prohibited under this section (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (2) In an action brought by a person aggrieved under this section against a covered entity who has engaged in unlawful discrimination based on disparate impact prohibited under this section (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (3) Equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs shall be available in all cases brought for the failure to provide reasonable accommodations or reasonable modifications, or the failure to comply with requirements of effective communication, accessible design, maintenance of accessible features, or program accessibility. (4) In any settlement agreement or consent decree to resolve an action brought or which may be brought under this section, attorney\u2019s fees of the plaintiff shall be included. .\n##### (e) Fair Housing Act\nThe Fair Housing Act (title VIII of the Civil Rights Act of 1968; 42 U.S.C. 3601 et seq. ), as amended by this Act, is further amended by adding at the end the following:\n823. Disparate impact (a) In general (1) Establishment Discrimination (including exclusion from participation and denial of benefits) based on disparate impact is established under this title only if\u2014 (A) a person aggrieved by discrimination on the basis of race, color, sex, or national origin demonstrates that an entity subject to this title (referred to in this title as a covered entity ) has a policy or practice that causes a disparate impact on the basis of race, color, sex, or national origin and the covered entity fails to demonstrate that the challenged policy or practice is related to and necessary to achieve the nondiscriminatory goals of the program or activity alleged to have been operated in a discriminatory manner; or (B) the person aggrieved demonstrates that a less discriminatory alternative policy or practice exists, and the covered entity refuses to adopt such alternative policy or practice. (2) Demonstration (A) Causation With respect to demonstrating that a particular policy or practice causes a disparate impact as described in subsection (a)(1), the person aggrieved shall demonstrate that each particular challenged policy or practice causes a disparate impact, except that if the person aggrieved demonstrates to the court that the elements of a covered entity\u2019s decisionmaking process are not capable of separation for analysis, the decisionmaking process may be analyzed as 1 policy or practice. (B) No requirement To demonstrate If the covered entity demonstrates that a specific policy or practice does not cause the disparate impact, the covered entity shall not be required to demonstrate that such policy or practice is necessary to achieve the goals of its program or activity. (b) Necessity of intentional discrimination To achieve policy goals not a defense A demonstration that a policy or practice is necessary to achieve the goals of a program or activity may not be used as a defense against a claim of intentional discrimination under this title. (c) Definition In this section, the term demonstrates means meets the burdens of production and persuasion. 824. Relief for claims based on differing standards of proof (a) Claims Based on Proof of Intentional Discrimination In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful intentional discrimination (not a practice that is unlawful because of its disparate impact) prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (b) Claims Based on the Disparate Impact Standard of Proof In an action brought by a person aggrieved under this title against a covered entity who has engaged in unlawful discrimination based on disparate impact prohibited under this title (including its implementing regulations), the person aggrieved may recover equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs, except that punitive damages are not available against a government, government agency, or political subdivision. (c) Relief available Equitable and legal relief (including compensatory and punitive damages), attorney\u2019s fees (including expert fees), and costs shall be available in all cases brought for the failure to permit reasonable accommodations, make reasonable modifications, or design and construct accessible dwellings as required by section 804(f)(3)(C). (d) Settlement In any settlement agreement or consent decree to resolve an action brought or which may be brought under this title, attorney\u2019s fees of the plaintiff shall be included. .\n#### 5. Prohibition on discrimination by law enforcement\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nThe term governmental body means any department, agency, special purpose district, or other instrumentality of Federal, State, local, or Indian tribal government.\n**(2)**\nThe term Indian tribe has the meaning given the term in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 479a ).\n**(3)**\nThe term law enforcement agency means any Federal, State, local, or Indian tribal governmental body engaged in the prevention, detection, or investigation of violations of criminal, immigration, or customs laws.\n**(4)**\nThe term law enforcement agent means any Federal, State, local, or Indian tribal official responsible for enforcing criminal, immigration, or customs laws, including police officers and other agents of a law enforcement agency.\n**(5)**\nThe term profiling means the practice of a law enforcement agent or agency relying, to any degree, on actual or perceived race, ethnicity, national origin, religion, sex (as defined in section 208 of the Civil Rights Act of 1964), gender identity, or sexual orientation in selecting which individual to subject to routine or spontaneous investigatory activities or in deciding upon the scope and substance of law enforcement activity following any initial investigatory procedure, except when there is trustworthy information, relevant to the locality and timeframe, that links a person with a particular characteristic described in this paragraph to an identified criminal incident or scheme.\n**(6)**\nThe term routine or spontaneous investigatory activities means the following activities by a law enforcement agent:\n**(A)**\nInterviews.\n**(B)**\nTraffic stops.\n**(C)**\nPedestrian stops.\n**(D)**\nFrisks and other types of body searches.\n**(E)**\nConsensual or nonconsensual searches of the persons, property, or possessions (including vehicles) of individuals using any form of public or private transportation, including motorists and pedestrians.\n**(F)**\nData collection, analysis, assessments, and predicated investigations.\n**(G)**\nInspections and interviews of entrants into the United States that are more extensive than those customarily carried out.\n**(H)**\nImmigration-related workplace investigations.\n**(I)**\nSuch other types of law enforcement encounters compiled for or by the Federal Bureau of Investigation or the Department of Justice Bureau of Justice Statistics.\n**(7)**\nThe term State means each of the 50 States, the District of Columbia, the Commonwealth of Puerto Rico, and any other territory or possession of the United States.\n**(8)**\nThe term unit of local government means\u2014\n**(A)**\nany city, county, township, town, borough, parish, village, or other general purpose political subdivision of a State;\n**(B)**\nany law enforcement district or judicial enforcement district that\u2014\n**(i)**\nis established under applicable State law; and\n**(ii)**\nhas the authority to, in a manner independent of other State entities, establish a budget and impose taxes; or\n**(C)**\nany Indian tribe that performs law enforcement functions, as determined by the Secretary of the Interior.\n##### (b) Prohibition of profiling\n**(1) In general**\nNo law enforcement agent or law enforcement agency shall engage in profiling.\n**(2) Enforcement**\n**(A) Remedy**\nThe United States, or an individual injured by profiling, may enforce this title in a civil action for equitable or legal relief, filed in a State court of general jurisdiction or in a district court of the United States.\n**(B) Parties**\nIn any action brought under this title, relief may be obtained against\u2014\n**(i)**\nany governmental body that employed any law enforcement agent who engaged in profiling;\n**(ii)**\nany agent of such body who engaged in profiling; and\n**(iii)**\nany person with supervisory authority over such agent.\n**(C) Nature Of Proof**\nProof that the routine or spontaneous investigatory activities of law enforcement agents in a jurisdiction have had a disparate impact on individuals with a particular characteristic described in subsection (a)(5) shall constitute prima facie evidence of a violation of this section.\n**(D) Attorney\u2019s Fees**\nIn any action or proceeding to enforce this section against any governmental body, the court may allow a prevailing plaintiff, other than the United States, reasonable attorney\u2019s fees as part of the costs, and may include expert fees as part of the attorney\u2019s fees.\n#### 6. Public accommodations\n##### (a) Prohibition on discrimination or segregation in public accommodations\nSection 201 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a ) is amended\u2014\n**(1)**\nin subsection (a), by inserting sex, before or national origin ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by striking stadium and all that follows and inserting stadium or other place or establishment that provides exhibition, entertainment, recreation, exercise, amusement, gathering, or display; ;\n**(B)**\nby redesignating paragraph (4) as paragraph (6); and\n**(C)**\nby inserting after paragraph (3) the following:\n(4) any establishment that provides a good, service, or program, including a store, shopping center, online retailer or service provider, salon, bank, gas station, food bank, service or care center, shelter, travel agency, funeral parlor, or any establishment that provides health care, accounting, or legal services; (5) any train service, bus service, car service, taxi service, airline service, station, depot, or other place of or establishment that provides transportation service; and .\n##### (b) Prohibition on discrimination or segregation under law\nSection 202 of such Act ( 42 U.S.C. 2000a\u20131 ) is amended by inserting sex, before or national origin .\n##### (c) Definitions and rules of construction\nTitle II of such Act ( 42 U.S.C. 2000a et seq. ) is amended by adding at the end the following:\n208. Definitions and rules (a) Definitions (1) Race; color; religion; sex; sexual orientation; gender identity; national origin The term race , color , religion , sex (including sexual orientation and gender identity) , or national origin , used with respect to an individual, includes\u2014 (A) the race, color, religion, sex (including sexual orientation and gender identity), or national origin, respectively, of another person with whom the individual is associated or has been associated; (B) a perception or belief, even if inaccurate, concerning the race, color, religion, sex (including sexual orientation and gender identity), or national origin, respectively, of the individual; and (C) in the case of race, traits historically associated with race, including natural hair texture and protective hairstyles. (2) Gender identity The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth. (3) Including The term including means including, but not limited to, consistent with the term\u2019s standard meaning in Federal law. (4) Natural hairstyles The term natural hair includes\u2014 (A) protective and natural hairstyles, which includes braids, locs, weaves, twists, afros; and (B) natural hair texture, which includes wavy, kinky, curl, and coily, and also the variation of texture in between. (5) Sex The term sex includes\u2014 (A) a sex stereotype; (B) pregnancy, childbirth, or a related medical condition; (C) sexual orientation or gender identity; and (D) sex characteristics, including intersex traits. (6) Sexual orientation The term sexual orientation means an individual\u2019s actual or perceived romantic, physical, or sexual attraction to other persons, or lack thereof, that includes heterosexuality, homosexuality, and bisexuality. (b) Rules In providing a remedy under this Act: (1) In the case of any conduct alleged to be discriminatory on the basis of sex, the remedy under this Act for such conduct, to the extent it pertains to pregnancy, childbirth, or a related medical condition may not result in a less substantial remedy than any other remedy for discrimination on the basis of sex. (2) In the case of any conduct alleged to be discriminatory on the basis of sex (with respect to gender identity), an individual shall not be denied access to a shared facility, including a restroom, a locker room, and a dressing room, that is in accordance with the individual\u2019s gender identity. 209. Rules of construction (a) Claims and remedies not precluded Nothing in this title shall be construed to limit the claims or remedies available to any individual for an unlawful practice on the basis of race, color, religion, sex, or national origin including claims brought pursuant to section 1979 or 1980 of the Revised Statutes ( 42 U.S.C. 1983 , 1985) or any other law, including the Federal law amended by the Customer Non-Discrimination Act, regulation, or policy. (b) No negative inference Nothing in this title shall be construed to support any inference that any Federal law prohibiting a practice on the basis of sex does not prohibit discrimination on the basis of pregnancy, childbirth, or a related medical condition, sexual orientation, gender identity, or a sex stereotype. (c) Scope of an establishment A reference in this title to an establishment\u2014 (1) shall be construed to include an individual whose operations affect commerce and who is a provider of a good, service, or program; and (2) shall not be construed to be limited to a physical facility or place. 210. Claims The Religious Freedom Restoration Act of 1993 ( 42 U.S.C. 2000bb et seq. ) shall not provide a claim concerning, or a defense to a claim under this title or provide a basis for challenging the application or enforcement of this title. .\n#### 7. Strict vicarious employer liability and Faragher-Ellerth affirmative defense removed\nSection 706 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20135 et seq. ) is amended by adding at the end the following:\n(l) An employer shall be liable for any act of discrimination prohibited under this title (including harassment, intimidation, or retaliation) committed by any of its employees. (m) It shall not be a defense to a claim under this title or provide a basis for challenging the application or enforcement of this title\u2014 (1) that an employer exercised reasonable care in attempting to prevent or took corrective action regarding any act of discrimination on the basis of sex (including intimidation, harassment, or retaliation); (2) that adverse employment action was not taken by such an employer; or (3) that an employee affected by that act did not take advantage of preventive opportunities to avoid harm. .\n#### 8. Arbitration of employment, consumer, and civil rights disputes\n##### (a) Purposes\nThe purposes of this section are to\u2014\n**(1)**\nprohibit predispute arbitration agreements that force arbitration of future employment, consumer, or civil rights disputes; and\n**(2)**\nprohibit agreements and practices that interfere with the right of individuals, workers, and small businesses to participate in a joint, class, or collective action related to an employment, consumer, or civil rights dispute.\n##### (b) In general\nTitle 9 of the United States Code is amended by adding at the end the following:\n4 ARBITRATION OF EMPLOYMENT, CONSUMER, AND CIVIL RIGHTS DISPUTES 401. Definitions In this chapter\u2014 (1) the term civil rights dispute means a dispute\u2014 (A) arising from an alleged violation of\u2014 (i) the Constitution of the United States or the constitution of a State; and (ii) any Federal, State, or local law that prohibits discrimination on the basis of race, sex, age, gender identity, sexual orientation, disability, religion, national origin, or any legally protected status in education, employment, credit, housing, public accommodations and facilities, voting, veterans or servicemembers, health care, or a program funded or conducted by the Federal Government or State government, including any law referred to or described in section 62(e) of the Internal Revenue Code of 1986, including parts of such law not explicitly referenced in such section but that relate to protecting individuals on any such basis; and (B) in which at least one party alleging a violation described in subparagraph (A) is one or more individuals (or their authorized representative), including one or more individuals seeking certification as a class under rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law; (2) the term consumer dispute means a dispute between\u2014 (A) one or more individuals who seek or acquire real or personal property, services (including services related to digital technology), securities or other investments, money, or credit for personal, family, or household purposes including an individual or individuals who seek certification as a class under rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law; and (B) (i) the seller or provider of such property, services, securities or other investments, money, or credit; or (ii) a third party involved in the selling, providing of, payment for, receipt or use of information about, or other relationship to any such property, services, securities or other investments, money, or credit; (3) the term employment dispute means a dispute between one or more individuals (or their authorized representative) and a person arising out of or related to the work relationship or prospective work relationship between them, including a dispute regarding the terms of or payment for, advertising of, recruiting for, referring of, arranging for, or discipline or discharge in connection with, such work, regardless of whether the individual is or would be classified as an employee or an independent contractor with respect to such work, and including a dispute arising under any law referred to or described in section 62(e) of the Internal Revenue Code of 1986, including parts of such law not explicitly referenced in such section but that relate to protecting individuals on any such basis, and including a dispute in which an individual or individuals seek certification as a class under rule 23 of the Federal Rules of Civil Procedure or as a collective action under section 16(b) of the Fair Labor Standards Act, or a comparable rule or provision of State law; (4) the term predispute arbitration agreement means an agreement to arbitrate a dispute that has not yet arisen at the time of the making of the agreement; and (5) the term predispute joint-action waiver means an agreement, whether or not part of a predispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not yet arisen at the time of the making of the agreement. 402. No validity or enforceability (a) In general Notwithstanding any other provision of this title, no predispute arbitration agreement or predispute joint-action waiver shall be valid or enforceable with respect to an employment dispute, consumer dispute, or civil rights dispute. (b) Applicability (1) In general An issue as to whether this chapter applies with respect to a dispute shall be determined under Federal law. The applicability of this chapter to an agreement to arbitrate and the validity and enforceability of an agreement to which this chapter applies shall be determined by a court, rather than an arbitrator, irrespective of whether the party resisting arbitration challenges the arbitration agreement specifically or in conjunction with other terms of the contract containing such agreement, and irrespective of whether the agreement purports to delegate such determinations to an arbitrator. (2) Collective bargaining agreements Nothing in this chapter shall apply to any arbitration provision in a contract between an employer and a labor organization or between labor organizations, except that no such arbitration provision shall have the effect of waiving the right of a worker to seek judicial enforcement of a right arising under a provision of the Constitution of the United States, a State constitution, or a Federal or State statute, or public policy arising therefrom. .\n##### (c) Technical and conforming amendments\n**(1) In general**\nTitle 9 of the United States Code is amended\u2014\n**(A)**\nin section 1 by striking of seamen, and all that follows through interstate commerce, and inserting in its place of individuals, regardless of whether such individuals are designated as employees or independent contractors for other purposes ;\n**(B)**\nin section 2 by inserting or as otherwise provided in chapter 4 before the period at the end;\n**(C)**\nin section 208\u2014\n**(i)**\nin the section heading by striking Chapter 1; residual application and inserting Application ; and\n**(ii)**\nby adding at the end the following: This chapter applies to the extent that this chapter is not in conflict with chapter 4. ; and\n**(D)**\nin section 307\u2014\n**(i)**\nin the section heading by striking Chapter 1; residual application and inserting Application ; and\n**(ii)**\nby adding at the end the following: This chapter applies to the extent that this chapter is not in conflict with chapter 4. .\n**(2) Table of sections**\n**(A) Chapter 2**\nThe table of sections of chapter 2 of title 9, United States Code, is amended by striking the item relating to section 208 and inserting the following:\n208. Application. .\n**(B) Chapter 3**\nThe table of sections of chapter 3 of title 9, United States Code, is amended by striking the item relating to section 307 and inserting the following:\n307. Application. .\n**(3) Table of chapters**\nThe table of chapters of title 9, United States Code, is amended by adding at the end the following:\n4. Arbitration of employment, consumer, antitrust, and civil rights disputes .\n#### 9. Liability of certain government officials\n##### (a) Amendment\nRevised Statute 1979 ( 42 U.S.C. 1983 ) is amended by inserting of the United States or before of any State .\n##### (b) Rules for application\nIn any action under Revised Statute 1979, the following shall apply:\n**(1) Definition of State**\nThe term State includes any person or entity that undertakes action under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia.\n**(2) Action under color of law**\nA private person or entity undertakes action under color of any statute, ordinance, regulation, custom, or usage, of the United States or of any State or Territory or the District of Columbia, when\u2014\n**(A)**\nundertaking a public function delegated by the United States or by a State or local government;\n**(B)**\nvoluntarily undertaking a public function;\n**(C)**\nacting in concert with the United States or a State or local government or acting in concert with an individual officer, agent, or entity of the United States or a State or local government;\n**(D)**\nengaging in joint action towards a common goal or plan with the United States or a State or local government or engaging in joint action towards a common goal or plan with an individual officer, agent, or entity of the United States or of a State or local government;\n**(E)**\nengaged in a conspiracy with the United States or a State or local government or engaged in a conspiracy with an individual officer, agent, or entity of the United States or of a State or local government;\n**(F)**\na close nexus exists between the private person or entity and the United States or a State or local government or a close nexus exists between an individual officer, agent, or entity of the United States or a State or local government;\n**(G)**\nthe activities of the private person or entity is so entwined with the United States or a State or local government or an individual officer, agent, or entity of the United States or of a State or local government such that the private person or entity is fairly considered to be acting under color of law; or\n**(H)**\notherwise exercises powers traditionally reserved to the United States or to State or local government.\n**(3) Presumption**\nA private person or entity is presumed to be acting under color of law when, pursuant to a contract or other legally binding agreement with the United States or with a State or local government, the private person or entity exercises any power of the United States or of that State or local government or the private person or entity otherwise undertakes the administration, operations, or other activities of: the judiciary, law enforcement, public education, jails or prisons, elections, municipal water services, municipal waste removal, evictions, public parks, or public benefits programs.\n**(4) No defense of qualified immunity**\nQualified immunity is not a defense in an action brought against any person who under color of any statute, ordinance, regulation, custom, or usage, of the United States or of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws.\n**(5) Respondeat superior**\nIn the case of any official of any political subdivision of the United States or of a State, if that official, acting under color of law, violates any provision of this Act, that official shall be amenable to any suit under this Act, and the political subdivision may be held liable for the acts of that official, whether acting in his or her official or individual capacity.\n#### 10. Explicit inclusion of rulemakings\nSection 1003(a)(1) of the Rehabilitation Act Amendments of 1986 ( 42 U.S.C. 2000d\u20137(a)(1) ) is amended by inserting before the period at the end the following: (including the provisions of any rule made to implement any of the foregoing statutes) .\n#### 11. Construction\n##### (a) Relief\nNothing in this Act, including any amendment made by this Act, shall be construed to limit the scope of, or the relief available under, section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), or any other provision of law.\n##### (b) Defendants\nNothing in this Act, including any amendment made by this Act, shall be construed to limit the scope of the class of persons who may be subjected to civil actions under the covered civil rights provisions.\n##### (c) Severability\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act and the application of the remaining provisions of this Act to any person or circumstance shall not be affected thereby.\n##### (d) Arbitration\nNothing in this Act, or the amendments made by this Act, shall be construed to prohibit the use of arbitration on a voluntary basis after a dispute arises.\n#### 12. Effective date\n##### (a) In General\nThis Act, and the amendments made by this Act, take effect on the date of enactment of this Act.\n##### (b) Application\nThis Act, and the amendments made by this Act, apply to all actions or proceedings pending on or after the date of enactment of this Act, and, in the case of section 8 and the amendments made thereby, shall apply with respect to any dispute or claim that arises or accrues on or after such date.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-09",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7005",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Customer Non-Discrimination Act",
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
            "name": "Age discrimination",
            "updateDate": "2025-07-08T12:40:55Z"
          },
          {
            "name": "Alternative dispute resolution, mediation, arbitration",
            "updateDate": "2025-07-08T12:42:57Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-07-08T12:42:25Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-08T12:40:28Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-07-08T12:41:41Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-07-08T12:40:50Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-07-08T12:42:52Z"
          },
          {
            "name": "Government liability",
            "updateDate": "2025-07-08T12:43:06Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-07-08T12:41:29Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-08T12:41:33Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-07-08T12:42:19Z"
          },
          {
            "name": "Public transit",
            "updateDate": "2025-07-08T12:42:15Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-08T12:40:40Z"
          },
          {
            "name": "Railroads",
            "updateDate": "2025-07-08T12:42:29Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-07-08T12:41:57Z"
          },
          {
            "name": "Service industries",
            "updateDate": "2025-07-08T12:41:52Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-07-08T12:40:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-14T14:52:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
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
          "measure-id": "id119hr1354",
          "measure-number": "1354",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1354v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Justice for All Act of 2025</strong></p><p>This bill prohibits discrimination based on sex, sexual orientation, gender identity, or race-related characteristics in schools, businesses, federally funded programs, and other settings. It also provides statutory authority for and expands the types of civil actions that may be brought for violations.</p><p>For example, the bill expands provisions under the Civil Rights Act of 1964 so as to (1) prohibit federally funded programs from discriminating based on sex or religion; and (2) prohibit public accommodations, including stores and transit services, from discriminating based on sex.</p><p>The bill defines <em>sex</em> to include sex stereotypes, pregnancy, childbirth, sexual orientation, gender identity, and sex characteristics. It also expands the definition of <em>race </em>to include traits that have been historically associated with race (e.g., natural hair textures). The expanded definitions apply to the Civil Rights Act of 1964, the Fair Housing Act (discrimination in public and private housing), and Title IX of the Education Amendments of 1972 (discrimination based on sex in federally funded educational programs).</p><p>Further, the bill provides statutory authority for disparate impact or intentional discrimination claims under the aforementioned acts, as well as the Age Discrimination Act of 1975 (discrimination based on age by federally funded programs) and the Rehabilitation Act of 1973 (discrimination based on disability by federally funded programs).</p><p>The bill also includes other provisions that address (1) profiling by law enforcement officers, (2) employer liability with respect to civil rights violations, (3) predispute arbitration agreements in civil rights cases, and (4) governmental immunity in suits involving constitutional violations.</p>"
        },
        "title": "Justice for All Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1354.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for All Act of 2025</strong></p><p>This bill prohibits discrimination based on sex, sexual orientation, gender identity, or race-related characteristics in schools, businesses, federally funded programs, and other settings. It also provides statutory authority for and expands the types of civil actions that may be brought for violations.</p><p>For example, the bill expands provisions under the Civil Rights Act of 1964 so as to (1) prohibit federally funded programs from discriminating based on sex or religion; and (2) prohibit public accommodations, including stores and transit services, from discriminating based on sex.</p><p>The bill defines <em>sex</em> to include sex stereotypes, pregnancy, childbirth, sexual orientation, gender identity, and sex characteristics. It also expands the definition of <em>race </em>to include traits that have been historically associated with race (e.g., natural hair textures). The expanded definitions apply to the Civil Rights Act of 1964, the Fair Housing Act (discrimination in public and private housing), and Title IX of the Education Amendments of 1972 (discrimination based on sex in federally funded educational programs).</p><p>Further, the bill provides statutory authority for disparate impact or intentional discrimination claims under the aforementioned acts, as well as the Age Discrimination Act of 1975 (discrimination based on age by federally funded programs) and the Rehabilitation Act of 1973 (discrimination based on disability by federally funded programs).</p><p>The bill also includes other provisions that address (1) profiling by law enforcement officers, (2) employer liability with respect to civil rights violations, (3) predispute arbitration agreements in civil rights cases, and (4) governmental immunity in suits involving constitutional violations.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr1354"
    },
    "title": "Justice for All Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for All Act of 2025</strong></p><p>This bill prohibits discrimination based on sex, sexual orientation, gender identity, or race-related characteristics in schools, businesses, federally funded programs, and other settings. It also provides statutory authority for and expands the types of civil actions that may be brought for violations.</p><p>For example, the bill expands provisions under the Civil Rights Act of 1964 so as to (1) prohibit federally funded programs from discriminating based on sex or religion; and (2) prohibit public accommodations, including stores and transit services, from discriminating based on sex.</p><p>The bill defines <em>sex</em> to include sex stereotypes, pregnancy, childbirth, sexual orientation, gender identity, and sex characteristics. It also expands the definition of <em>race </em>to include traits that have been historically associated with race (e.g., natural hair textures). The expanded definitions apply to the Civil Rights Act of 1964, the Fair Housing Act (discrimination in public and private housing), and Title IX of the Education Amendments of 1972 (discrimination based on sex in federally funded educational programs).</p><p>Further, the bill provides statutory authority for disparate impact or intentional discrimination claims under the aforementioned acts, as well as the Age Discrimination Act of 1975 (discrimination based on age by federally funded programs) and the Rehabilitation Act of 1973 (discrimination based on disability by federally funded programs).</p><p>The bill also includes other provisions that address (1) profiling by law enforcement officers, (2) employer liability with respect to civil rights violations, (3) predispute arbitration agreements in civil rights cases, and (4) governmental immunity in suits involving constitutional violations.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119hr1354"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1354ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Justice for All Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for All Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Civil Rights Act of 1964 to clarify that disparate impacts on certain populations constitute a sufficient basis for rights of action under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:04Z"
    }
  ]
}
```
