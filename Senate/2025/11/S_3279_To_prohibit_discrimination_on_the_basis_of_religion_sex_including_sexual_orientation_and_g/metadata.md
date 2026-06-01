# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3279?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3279
- Title: John Lewis Every Child Deserves a Family Act
- Congress: 119
- Bill type: S
- Bill number: 3279
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3279",
    "number": "3279",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Families"
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
    "title": "John Lewis Every Child Deserves a Family Act",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
            "date": "2025-11-20T21:21:19Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-20T21:21:19Z",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CO"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DE"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-11-20",
      "state": "VT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NH"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MD"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "AZ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3279is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3279\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mrs. Gillibrand (for herself, Mr. Schatz , Mr. Booker , Ms. Smith , Mr. Hickenlooper , Mr. Schiff , Mr. Merkley , Mr. Coons , Mr. Whitehouse , Mr. Van Hollen , Ms. Baldwin , Mr. Markey , Mr. Wyden , Ms. Duckworth , Ms. Rosen , Mr. Sanders , Mr. Murphy , Mr. Kaine , Mr. Blumenthal , Mr. Fetterman , Ms. Klobuchar , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit discrimination on the basis of religion, sex (including sexual orientation and gender identity), and marital status in the administration and provision of child welfare services, to improve safety, well-being, and permanency for lesbian, gay, bisexual, transgender, and queer or questioning foster youth, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the John Lewis Every Child Deserves a Family Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nEvery child or youth unable to live with their family of origin is entitled to a supportive and affirming foster care placement. Federal law requires, and child welfare experts recommend, that children and youth be placed with a family or in the most family-like setting available.\n**(2)**\nThousands of children and youth lack a stable, safe, and loving temporary or permanent home and have been placed in a congregate care setting, which is associated with more placements, poorer educational outcomes, and greater risk of further trauma. More homes are needed to accommodate the close to 400,000 children and youth who are in foster care nationwide, as of the date of enactment of this Act.\n**(3)**\nTitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) protects people from discrimination based on race, color, or national origin in programs, activities, and services administered or performed by child welfare agencies. Eliminating discrimination in child welfare based on religion, sex (including sexual orientation and gender identity), and marital status would increase the number and diversity of foster and adoptive homes able to meet the individual needs of children and youth removed from their homes.\n**(4)**\nLesbian, gay, bisexual, transgender, and queer or questioning (referred to in this Act as LGBTQ ) youth are overrepresented in the foster care system by at least a factor of 2, comprising at least 30 percent of children and youth in foster care. These numbers are higher for transgender and nonbinary youth compared to their cisgender LGBQ counterparts.\n**(A)**\nWhile some LGBTQ youth enter foster care for similar reasons as non-LGBTQ youth, the 2 most common reasons for LGBTQ youth are high rates of physical abuse and conflict with parents.\n**(B)**\nLGBTQ foster youth report twice the rate of poor treatment while in care experienced by foster youth who do not identify as LGBTQ and are more likely to experience discrimination, harassment, and violence in the child welfare system than their LGBTQ peers not in the child welfare system.\n**(C)**\nBecause of high levels of bias, LGBTQ foster youth have a higher average number of placements and higher likelihood of living in a group home than their non-LGBTQ peers, negatively affecting mental health outcomes and long-term prospects.\n**(D)**\nApproximately 28 percent of homeless youth with histories of time in foster care identified as LGBTQ and were significantly more likely to experience 7 of 8 adverse events, such as being physically harmed, or being stigmatized or discriminated against, compared to their peers with no foster care history.\n**(E)**\nLGBTQ youth in foster care had nearly 3 times greater odds of reporting a past-year suicide attempt compared to LGBTQ youth who were never in foster care (35 percent for those youth in foster care as compared to 13 percent for those youth who were never in foster care). These numbers were even higher for LGBTQ foster youth of color (38 percent) and highest for transgender and nonbinary foster youth (45 percent).\n**(F)**\nLGBTQ youth who had been in foster care had over 3 times greater odds of being kicked out, abandoned, or running away due to treatment based on their LGBTQ identity compared to those who were never in foster care (27 percent for those youth who had been in foster care as compared to 8 percent for those youth who had never been in foster care). These numbers were higher for LGBTQ foster youth of color (30 percent) and transgender and non-binary foster youth (40 percent).\n**(5)**\nConversion therapy is a form of discrimination that harms LGBTQ people. It undermines an individual\u2019s sense of self-worth, increases suicide ideation and substance abuse, exacerbates family conflict, and contributes to second-class status. No scientifically valid evidence supports this discredited practice, which is prohibited by many States and foreign nations. Approximately 350,000 LGBTQ adults were subjected to so-called conversion therapy as adolescents, and an estimated 16,000 LGBTQ youth ages 13 to 17 will be subjected to it by a licensed health care professional before age 18.\n**(6)**\nMany youth, especially LGBTQ youth, involved with child welfare services identify with a cross-section of marginalized communities. Youth of color are overrepresented in the foster care system, and the majority of LGBTQ foster youth are youth of color. Children and youth with multiple mar\u00adgin\u00ada\u00adlized identities often experience more stress and trauma than other youth, compounding the negative effects of discrimination and increasing the likelihood of negative outcomes.\n**(7)**\nProspective parents who experience the heartbreak and dignitary harm of discrimination based on religion, sex (including sexual orientation and gender identity), or marital status may not be able or willing to apply at another agency, resulting in fewer available homes, and knowing that discrimination exists may deter them from even attempting to foster or adopt.\n**(8)**\nProfessional organizations that serve children in the fields of medicine, psychology, law, and child welfare oppose discrimination against prospective parents in adoption and foster care.\n**(9)**\nReligious organizations play a critical role in providing child welfare services. Most welcome all children, youth, and families and affirm a diversity of religions and faiths. State assessments, planning, and counseling should connect children and youth for whom spirituality and religion are important with affirming, faith-based resources consistent with the faith of the child or youth.\n**(10)**\nChild welfare agencies that refuse to serve same-sex couples and LGBTQ individuals reduce the pool of qualified and available homes for children and youth who need placement on a temporary or permanent basis.\n**(A)**\nSame-sex couples are 7 times more likely to foster and adopt than their different-sex counterparts.\n**(B)**\nSame-sex couples raising adopted children tend to be older than, just as educated as, and have access to the same economic resources as other adoptive parents.\n**(C)**\nResearch shows that sexual orientation is a nondeterminative factor in parental success and that children with same-sex parents have the same advantages and expectations for health, social, and psychological development as children whose parents are different-sex.\n**(D)**\nDiscrimination against qualified prospective foster and adoptive parents for non-merit related reasons denies religious minority, LGBTQ, and unmarried relatives the opportunity to become foster and adoptive parents for their own kin in care, including grandchildren.\n**(11)**\nLGBTQ families of origin are at risk for discrimination in child welfare referrals, investigations, removals, reunification, kinship placements, and other case management services. A study of low-income African-American mothers showed that those who identified as lesbian or bisexual were 4 times more likely than their non-LGBTQ counterparts to lose custody of their children in child welfare proceedings. LGBTQ-positive services are necessary to shield families and protect parents\u2019 rights to reunification.\n**(12)**\nSingle people are more likely than couples to experience challenges in adopting due to biases that persist against single-parent adoption. During fiscal year 2022, 29 percent of adoptions from foster care were completed by unmarried single people, including adoptions by some 2000 single men and more than 13,000 single women. Studies show that the outcomes for children adopted and raised by single parents are just as good as, if not better than, outcomes for children adopted by couples.\n**(13)**\nMore nationwide data about the experiences of LGBTQ children and youth involved with child welfare services is needed to understand fully the extent and impact of discrimination and ensure accountability. States must report and researchers must collect this sensitive data in an ethical, affirming, and non-intrusive manner, with appropriate safeguards to protect respondents.\n##### (b) Purpose\nThe purposes of this Act are\u2014\n**(1)**\nto prohibit discrimination on the basis of religion, sex (including sexual orientation and gender identity), and marital status in the administration and provision of child welfare services that receive Federal funds; and\n**(2)**\nto improve safety, well-being, and permanency for LGBTQ children and youth involved with child welfare services.\n#### 3. Every child deserves a family\n##### (a) Prohibition\nNo child or youth involved with child welfare services, family, or individual shall, on the grounds of religion, sex (including sexual orientation and gender identity), or marital status, be excluded from participation in, denied the benefits of, or be subjected to discrimination in the administration or provision of child welfare programs and services by a covered entity.\n##### (b) Private right of action\nAny individual who is aggrieved by a violation of this Act may bring a civil action seeking relief in an appropriate United States district court. The court shall award a plaintiff prevailing in such an action all appropriate relief, including injunctive, declaratory, and other equitable relief necessary to carry out this Act, attorneys\u2019 fees, and such other relief as the court determines appropriate.\n##### (c) Federal guidance\nNot later than 6 months after the date of the enactment of this Act, the Secretary shall publish and disseminate guidance with respect to compliance with this Act.\n##### (d) Technical assistance\nIn order to ensure compliance with and understanding of the legal, practice, and cultural changes required by this Act, the Secretary shall provide technical assistance to all covered entities, including\u2014\n**(1)**\nidentifying State laws and regulations inconsistent with this Act, and providing guidance and training to ensure the State laws and regulations are brought into compliance with this Act by the applicable compliance deadline in effect under subsection (h);\n**(2)**\nidentifying casework practices and procedures inconsistent with this Act and providing guidance and training to ensure the practices and procedures are brought into compliance with this Act by the applicable compliance deadline;\n**(3)**\nproviding guidance in expansion of recruitment efforts to ensure consideration of all prospective adoptive and foster parents regardless of the religion, sex (including sexual orientation and gender identity), or marital status of the prospective parent;\n**(4)**\ncreating comprehensive cultural competency training for covered entities and prospective adoptive and foster parents; and\n**(5)**\ntraining judges and attorneys involved in foster care, guardianship, and adoption cases on the findings and purposes of this Act.\n##### (e) Service delivery and training\n**(1) In general**\nA covered entity shall provide service delivery to children and youth involved with child welfare services, families, and adults, and staff training, that\u2014\n**(A)**\ncomprehensively addresses the individual strengths and needs of children and youth involved with child welfare services; and\n**(B)**\nis language appropriate, gender appropriate, and culturally sensitive and respectful of the complex social identities of the children and youth, families, and adults currently or prospectively participating in or receiving child welfare services.\n**(2) Social identity**\nIn this subsection, the term social identity includes an individual\u2019s race, ethnicity, nationality, age, religion (including spirituality), sex (including gender identity and sexual orientation), socioeconomic status, physical or cognitive ability, language, beliefs, values, behavior patterns, and customs.\n##### (f) Data collection\nUsing developmentally appropriate best practices, the Secretary shall collect data through the Adoption and Foster Care Analysis and Reporting System on\u2014\n**(1)**\nthe sexual orientation and gender identity of children and youth involved with child welfare services and foster and adoptive parents; and\n**(2)**\nwhether family conflict related to the sexual orientation or gender identity of a child or youth was a factor in the removal of the child or youth from the family.\n##### (g) National Resource Center on Safety, Well-Being, Placement Stability, and Permanency for LGBTQ Children and Youth Involved with Child Welfare Services\n**(1) In general**\nThe Secretary shall establish and maintain the National Resource Center on Safety, Well-Being, Placement Stability, and Permanency for LGBTQ Children and Youth Involved with Child Welfare Services (referred to in this Act as the National Resource Center ) that will promote well-being, safety, permanency, stability, and family placement for LGBTQ children and youth involved with child welfare services, through training, technical assistance, actions, and guidance that\u2014\n**(A)**\nincrease LGBTQ cultural competency among the staff of covered entities, and foster, adoptive, and relative parents, guardians, and caregivers;\n**(B)**\npromote the provision of child welfare services that address the specific needs of LGBTQ children and youth involved with child welfare services and their families;\n**(C)**\npromote effective and responsible collection and management of data on the sexual orientation and gender identity of children and youth in the child welfare system, with appropriate safeguards to protect the data;\n**(D)**\nidentify and promote promising practices and evidence-based models of engagement and appropriate collective and individual services and interventions that can be linked to improved outcomes for LGBTQ children and youth in the child welfare system;\n**(E)**\nendorse best practices for human resource activities of covered entities, including in hiring, staff development, and implementing a system of accountability to carry out those best practices; and\n**(F)**\ninitiate other actions that improve safety, well-being, placement stability, and permanency outcomes for LGBTQ children and youth involved with child welfare services at the State and local level.\n**(2) Activities**\nThe Secretary shall carry out the collection and analysis of data and the dissemination of research to carry out this subsection.\n**(3) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary such sums as may be necessary to establish and maintain the National Resource Center and carry out the activities described in this subsection.\n##### (h) Deadline for compliance\n**(1) In general**\nExcept as provided in paragraph (2), a covered entity shall comply with this section not later than 6 months after publication of the guidance referred to in subsection (c), or 1 year after the date of the enactment of this Act, whichever occurs first.\n**(2) Authority to extend deadline**\nIf a State demonstrates to the satisfaction of the Secretary that it is necessary to amend State law in order to change a particular practice that is inconsistent with this Act, the Secretary may extend the compliance date for the State and any covered entities in the State a reasonable number of days after the close of the first State legislative session beginning after the date the guidance referred to in subsection (c) is published.\n**(3) Authority to withhold funds**\nIf the Secretary finds that a covered entity has failed to comply with this Act, the Secretary may withhold payment to the State of amounts otherwise payable to the State under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. ; 42 U.S.C. 670 et seq. ), to the extent determined by the Secretary.\n##### (i) GAO study\n**(1) In general**\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall conduct a study to determine whether the States have substantially complied with this Act, including specifically whether the States have\u2014\n**(A)**\neliminated all policies, practices, or laws that permit a covered entity to violate subsection (a);\n**(B)**\nprovided necessary training and technical support to covered entities to ensure all services to children and youth involved with child welfare services are carried out in a non-discriminatory, affirming, safe, and culturally competent manner;\n**(C)**\ncollected data necessary to accomplishing the purposes of this Act, and ensured that the data is appropriately safeguarded, including data related to\u2014\n**(i)**\nthe sexual orientation and gender identity of children and youth involved with child welfare services;\n**(ii)**\nthe permanency and placement outcomes and rates for those children and youth, as compared to their non-LGBTQ peers;\n**(iii)**\nthe rates at which those children and youth are placed in family homes as compared to congregate or group homes; and\n**(iv)**\nthe sexual orientation, gender identity, and marital status of foster and adoptive parents, as well as the placement rates and wait periods for those foster and adoptive parents; and\n**(D)**\nensured that covered entities\u2014\n**(i)**\nare in compliance with this Act; and\n**(ii)**\nhave implemented procedures for children and youth involved with child welfare services, or individuals or families participating in, or seeking to participate in, child welfare services, to report violations of this Act.\n**(2) Report to the Congress**\nNot later than 6 months after completing the study required by paragraph (1), the Comptroller General shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a written report that contains the results of the study.\n##### (j) Relation to other laws\n**(1) Rule of construction**\nNothing in this Act shall be construed to invalidate or limit rights, remedies, or legal standards under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n**(2) Certain claims**\nThe Religious Freedom Restoration Act of 1993 ( 42 U.S.C. 2000bb et seq. ) shall not provide a claim concerning, or a defense to a claim under, this Act, or provide a basis for challenging the application or enforcement of this Act.\n##### (k) Definitions\nIn this section:\n**(1) Child or youth involved with child welfare services**\nThe term child or youth involved with child welfare services means an individual, aged 23 or younger, who participates in child welfare programs or services that receive Federal financial assistance under part A, B, or E of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ; 42 U.S.C. 621 et seq. ; 42 U.S.C. 670 et seq. ), title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or title XX of the Social Security Act ( 42 U.S.C. 1397 et seq. ).\n**(2) Conversion therapy**\n**(A) In general**\nThe term conversion therapy means a form of discrimination that includes any practice or treatment which seeks to change the sexual orientation or gender identity of an individual, including efforts to change behaviors or gender expressions or to eliminate or reduce sexual or romantic attractions or feelings toward individuals of the same gender.\n**(B) Exclusions**\nThe term conversion therapy does not include counseling that provides assistance to an individual undergoing gender transition, or counseling that provides acceptance, support, and understanding of an individual or facilitates an individual with coping, social support, and identity exploration and development, including sexual orientation-neutral interventions to prevent or address unlawful conduct or unsafe sexual practices.\n**(3) Covered entity**\nThe term covered entity means an entity that\u2014\n**(A)**\nreceives Federal financial assistance under part A, B, or E of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ; 42 U.S.C. 621 et seq. ; 42 U.S.C. 670 et seq. ), title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or title XX of the Social Security Act ( 42 U.S.C. 1397 et seq. ); and\n**(B)**\nis involved in the administration or provision of child welfare programs or services.\n**(4) Gender identity**\nThe term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the designated sex of the individual at birth.\n**(5) Religion; sex (including sexual orientation and gender identity), or marital status**\nThe term religion, sex (including sexual orientation and gender identity), or marital status , used with respect to an individual, includes\u2014\n**(A)**\nthe religion, sex (including sexual orientation and gender identity), or marital status, respectively, of another person with whom the individual is or has been associated; and\n**(B)**\na perception or belief, even if inaccurate, concerning the religion, sex (including sexual orientation and gender identity), or marital status, respectively, of the individual.\n**(6) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(7) Sex**\nThe term sex includes\u2014\n**(A)**\na sex stereotype;\n**(B)**\npregnancy, childbirth, or a related medical condition;\n**(C)**\nsexual orientation or gender identity; and\n**(D)**\nsex characteristics, including intersex traits.\n**(8) Sexual orientation**\nThe term sexual orientation means homosexuality, heterosexuality, or bisexuality.\n**(9) State**\nThe term State means each of the 50 States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6181",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "John Lewis Every Child Deserves a Family Act",
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
        "name": "Families",
        "updateDate": "2026-01-05T14:51:22Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3279is.xml"
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
      "title": "John Lewis Every Child Deserves a Family Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "John Lewis Every Child Deserves a Family Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit discrimination on the basis of religion, sex (including sexual orientation and gender identity), and marital status in the administration and provision of child welfare services, to improve safety, well-being, and permanency for lesbian, gay, bisexual, transgender, and queer or questioning foster youth, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:51Z"
    }
  ]
}
```
