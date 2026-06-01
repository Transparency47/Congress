# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3508
- Title: End Diaper Need Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3508
- Origin chamber: House
- Introduced date: 2025-05-20
- Update date: 2026-05-22T08:08:38Z
- Update date including text: 2026-05-22T08:08:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-20: Introduced in House

## Actions

- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3508",
    "number": "3508",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "End Diaper Need Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:38Z",
    "updateDateIncludingText": "2026-05-22T08:08:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-20",
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
          "date": "2025-05-20T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-20T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "IN"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "GA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MS"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3508ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3508\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2025 Ms. DeLauro (for herself, Mrs. Watson Coleman , and Mrs. Foushee ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide targeted funding for States and other eligible entities through the Social Services Block Grant program to address the increased burden that maintaining the health and hygiene of infants and toddlers, medically complex children, and low-income adults or adults with disabilities who rely on adult incontinence materials and supplies place on families in need, the resultant adverse health effects on children and families, and the limited child care options available for infants and toddlers who lack sufficient diapers and diapering supplies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Diaper Need Act of 2025 .\n#### 2. Targeted funding for diaper assistance (including diapering supplies and adult incontinence materials and supplies) through the Social Services Block Grant Program\n##### (a) Increase in funding for Social Services Block Grant Program\n**(1) In general**\nThe amount specified in subsection (c) of section 2003 of the Social Security Act ( 42 U.S.C. 1397b ) for purposes of subsections (a) and (b) of such section is deemed to be $1,900,000,000 for each of fiscal years 2026 through 2029. Each State shall use the increase in funding the State receives as a result of this section in accordance with subsection (b) of this section.\n**(2) Appropriation**\n**(A) In general**\nOut of any money in the Treasury of the United States not otherwise appropriated, there is appropriated $200,000,000 for each of fiscal years 2026 through 2029, to carry out this section.\n**(B) Reservations**\n**(i) Purposes**\nThe Secretary shall reserve, from the amount appropriated under subparagraph (A) to carry out this section\u2014\n**(I)**\nfor each of fiscal years 2026 through 2029, not more than 2 percent of the amount appropriated for the fiscal year for purposes of entering into an agreement with a national entity described in subparagraph (C) to assist in providing technical assistance and training, to support effective policy, practice, research, and cross-system collaboration among grantees and subgrantees, and to assist in the administration of the program described in this section; and\n**(II)**\nfor fiscal year 2026, an amount, not to exceed $3,000,000, for purposes of conducting an evaluation under subsection (d).\n**(ii) No State entitlement to reserved funds**\nThe State entitlement under section 2002(a) of the Social Security Act ( 42 U.S.C. 1397a(a) ) shall not apply to the amounts reserved under clause (i).\n**(C) National entity described**\nA national entity described in this subparagraph is a nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code, that\u2014\n**(i)**\nhas experience in more than 1 State in the area of\u2014\n**(I)**\ncommunity distributions of basic need services, including experience collecting, warehousing, and distributing basic necessities such as diapers, food, or menstrual products;\n**(II)**\nchild care;\n**(III)**\nchild development activities in low-income communities; or\n**(IV)**\nmotherhood, fatherhood, or parent education efforts serving low-income parents of young children;\n**(ii)**\ndemonstrates competency to implement a project, provide fiscal accountability, collect data, and prepare reports and other necessary documentation; and\n**(iii)**\ndemonstrates a willingness to share information with researchers, practitioners, and other interested parties.\n##### (b) Rules governing use of additional funds\n**(1) In general**\nFunds are used in accordance with this subsection if\u2014\n**(A)**\nthe State, in consultation with relevant stakeholders, including agencies, professional associations, and nonprofit organizations, distributes the funds to eligible entities to\u2014\n**(i)**\ndecrease the need for diapers and diapering supplies and adult incontinence materials and supplies in low-income families and meet such unmet needs of infants and toddlers, medically complex children, and low-income adults and adults with disabilities in such families through\u2014\n**(I)**\nthe distribution of free diapers and diapering supplies, medically necessary diapers, and adult incontinence materials and supplies; and\n**(II)**\nimproving access to diapers and diapering supplies, medically necessary diapers, and adult incontinence materials and supplies;\n**(ii)**\ncarry out community outreach to assist in participation in diaper distribution programs or programs that distribute medically necessary diapers or adult incontinence materials and supplies; and\n**(iii)**\nincrease the ability of communities and low-income families in such communities to provide for the need for diapers and diapering supplies, medically necessary diapers, and adult continence materials and supplies, of infants and toddlers, medically complex children, and low-income adults and adults with disabilities;\n**(B)**\nthe funds are used subject to the limitations in section 2005 of the Social Security Act ( 42 U.S.C. 1397d ); and\n**(C)**\nthe funds are used to supplement, not supplant, State general revenue funds provided for the purposes described in subparagraph (A).\n**(2) Administrative costs**\nA State receiving funds made available under subsection (a) may use not more than 5 percent of the funds for State administrative costs, which may include costs of contracting, monitoring, and reporting.\n**(3) Allowable uses by eligible entities**\nAn eligible entity receiving funds made available under subsection (a) shall use the funds for any of the following:\n**(A)**\nTo pay for the purchase and distribution of diapers and diapering supplies, medically necessary diapers, and funding diaper (including medically necessary diapers) distribution that serves low-income families with\u2014\n**(i)**\n1 or more children 3 years of age or younger; or\n**(ii)**\n1 or more medically complex children.\n**(B)**\nTo pay for the purchase and distribution of adult incontinence materials and supplies and funding distribution of the materials and supplies for low-income families with 1 or more low-income adults, adults with disabilities, or children with a disability who have attained 3 years of age and have not attained 19 years of age, who rely on adult incontinence materials and supplies.\n**(C)**\nTo integrate activities carried out under subparagraph (A) with other basic needs assistance programs serving eligible children and their families, including the following:\n**(i)**\nPrograms funded by the temporary assistance for needy families program under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ), including the State maintenance of effort provisions of such program.\n**(ii)**\nPrograms designed to support the health of eligible children, such as the Children\u2019s Health Insurance Program under title XXI of the Social Security Act, the Medicaid program under title XIX of such Act, or State funded health care programs.\n**(iii)**\nPrograms funded through the special supplemental nutrition program for women, infants, and children under section 17 of the Child Nutrition Act of 1966.\n**(iv)**\nPrograms that offer early home visiting services, including the maternal, infant, and early childhood home visiting program (including the Tribal home visiting program) under section 511 of the Social Security Act ( 42 U.S.C. 711 ).\n**(v)**\nPrograms to provide improved and affordable access to child care, including programs funded through the Child Care and Development Fund, the temporary assistance for needy families program under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ), or a State-funded program.\n**(vi)**\nPrograms funded under part C of the Individuals with Disabilities Education Act ( 20 U.S.C. 1431 et seq. ).\n**(4) Availability of funds**\n**(A) Funds distributed to eligible entities**\nFunds made available under subsection (a) that are distributed to an eligible entity by a State for a fiscal year may be expended by the eligible entity only in such fiscal year or the succeeding fiscal year.\n**(B) Evaluation**\nFunds reserved under subsection (a)(2)(B)(i)(II) to carry out the evaluation under subsection (d) shall be available for expenditure during the 3-year period that begins on the date of enactment of this Act.\n**(5) No effect on other programs**\nAny assistance or benefits received by a family through funds made available under subsection (a) shall be disregarded for purposes of determining the family\u2019s eligibility for, or amount of, benefits under any other Federal needs-based programs.\n##### (c) Annual reports\nA State shall include in the annual report required under section 2006 of the Social Security Act ( 42 U.S.C. 1397e ) covering each of fiscal years 2026 through 2029, information detailing how eligible entities, including subgrantees, used funds made available under subsection (a) to distribute diapers and diapering supplies and adult incontinence materials and supplies to families in need. Each such report shall include the following:\n**(1)**\nThe number and age of infants, toddlers, medically complex children, and low-income adults and adults with disabilities who received assistance or benefits through such funds.\n**(2)**\nThe number of families that have received assistance or benefits through such funds.\n**(3)**\nThe number of diapers, medically necessary diapers, or adult incontinence materials and supplies (such as adult diapers, briefs, protective underwear, pull-ons, pull-ups, liners, shields, guards, pads, undergarments), and the number of each type of diapering or adult incontinence supply, distributed through the use of such funds.\n**(4)**\nThe ZIP Code or ZIP Codes where the eligible entity (or subgrantee) distributed diapers and diapering supplies and adult incontinence materials and supplies.\n**(5)**\nThe method or methods the eligible entity (or subgrantee) uses to distribute diapers and diapering supplies and, adult incontinence materials and supplies.\n**(6)**\nSuch other information as the Secretary may specify.\n##### (d) Evaluation\nThe Secretary, in consultation with States, the national entity described in subsection (a)(2)(C), and eligible entities receiving funds made available under this section, shall\u2014\n**(1)**\nnot later than 2 years after the date of enactment of this Act\u2014\n**(A)**\ncomplete an evaluation of the effectiveness of the assistance program carried out pursuant to this section, such as the effect of activities carried out under this Act on mitigating the health and developmental risks of unmet diaper need among infants, toddlers, medically complex children, and other family members in low-income families, including the risks of diaper dermatitis, urinary tract infections, and parental and child depression and anxiety;\n**(B)**\nsubmit to the relevant congressional committees a report on the results of such evaluation; and\n**(C)**\npublish the results of the evaluation on the internet website of the Department of Health and Human Services;\n**(2)**\nnot later than 3 years after the date of enactment of this Act, update the evaluation required by paragraph (1)(A); and\n**(3)**\nnot later than 120 days after completion of the updated evaluation under paragraph (2)\u2014\n**(A)**\nsubmit to the relevant congressional committees a report describing the results of such updated evaluation; and\n**(B)**\npublish the results of such evaluation on the internet website of the Department of Health and Human Services.\n##### (e) Guidance\nNot later than 180 days after enactment of this Act, the Secretary shall issue guidance regarding how the provisions of this section should be carried out, including information regarding eligible entities, allowable use of funds, and reporting requirements.\n##### (f) Definitions\nIn this section:\n**(1) Adult incontinence materials and supplies**\nThe term adult incontinence materials and supplies means those supplies that are used to assist adults or adults with disabilities and includes adult diapers, briefs, protective underwear, pull-ons, pull-ups, liners, shields, guards, pads, undergarments, disposable wipes, over-the-counter adult diaper rash cream products, intermittent catheterization, indwelling catheters, condom catheters, urinary drainage bags, external collection devices, wearable urinals, and penile clamps.\n**(2) Adults with disabilities**\nThe term adults with disabilities means individuals who\u2014\n**(A)**\nhave attained 18 years of age; and\n**(B)**\nhave a disability (as such term is defined, with respect to an individual, in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 )).\n**(3) Diaper**\nThe term diaper means an absorbent garment that\u2014\n**(A)**\nis washable or disposable that may be worn by an infant or toddler who is not toilet-trained; and\n**(B)**\nif disposable\u2014\n**(i)**\ndoes not use any latex or common allergens; and\n**(ii)**\nmeets or exceeds the quality standards for diapers commercially available through retail sale in the following categories:\n**(I)**\nAbsorbency (with acceptable rates for first and second wetting).\n**(II)**\nWaterproof outer cover.\n**(III)**\nFlexible leg openings.\n**(IV)**\nRefastening closures.\n**(4) Diaper bank**\n- The term diaper bank means a nonprofit organization that\u2014\n**(A)**\nis described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code;\n**(B)**\nis established and operating primarily for the purpose of collecting or purchasing diapers and diapering supplies; and\n**(C)**\ndistributes diapers and diapering supplies either directly or through partnerships for eventual distribution to individuals free of charge.\n**(5) Diapering supplies**\nThe term diapering supplies means items, including diaper wipes and diaper cream, necessary to ensure that\u2014\n**(A)**\nan eligible child using a diaper is properly cleaned and protected from diaper rash; or\n**(B)**\na medically complex child who uses a medically necessary diaper is properly cleaned and protected from diaper rash.\n**(6) Eligible child**\nThe term eligible child means a child who\u2014\n**(A)**\nhas not attained 4 years of age; and\n**(B)**\nis a member of a low-income family.\n**(7) Eligible entities**\nThe term eligible entity means a State or local governmental entity, an Indian tribe or tribal organization (as defined in section 4 of the Indian Self-Determination and Education Assistance Act), or a diaper bank or other nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code that\u2014\n**(A)**\nhas at least 1 year of demonstrated experience in the area of\u2014\n**(i)**\ncommunity distributions of diapers and diapering supplies and other basic need services, such as food or menstrual products;\n**(ii)**\nchild care;\n**(iii)**\nchild development activities in low-income communities; or\n**(iv)**\nmotherhood, fatherhood, or parent education efforts serving low-income parents of young children;\n**(B)**\ndemonstrates competency to implement a project, provide fiscal accountability, collect data, and prepare reports and other necessary documentation; and\n**(C)**\ndemonstrates a willingness to share information with researchers, practitioners, and other interested parties.\n**(8) Federal poverty line**\nThe term Federal poverty line means the Federal poverty line as defined by the Office of Management and Budget and revised annually in accordance with section 673(2) of the Omnibus Budget Reconciliation Act of 1981 ( 42 U.S.C. 9902(2) ) applicable to a family of the size involved.\n**(9) Low-income**\nThe term low-income , with respect to a family, means a family whose self-certified income is not more than 200 percent of the Federal poverty line.\n**(10) Medically complex child**\nThe term medically complex child means an individual who has attained 3 years of age and for whom a licensed health care provider has provided a diagnosis of 1 or more significant chronic conditions.\n**(11) Medically necessary diaper**\nThe term medically necessary diaper means an absorbent garment that is\u2014\n**(A)**\nwashable or disposable;\n**(B)**\nworn by a medically complex child who has been diagnosed with bowel or bladder incontinence, a bowel or bladder condition that causes excess urine or stool (such as short gut syndrome or diabetes insipidus), or a severe skin condition that causes skin erosions (such as epidermolysis bullosa) and needs such garment to correct or ameliorate such condition; and\n**(C)**\nif disposable\u2014\n**(i)**\ndoes not use any latex or common allergens; and\n**(ii)**\nmeets or exceeds the quality standards for diapers commercially available through retail sale in the following categories:\n**(I)**\nAbsorbency (with acceptable rates for first and second wetting).\n**(II)**\nWaterproof outer cover.\n**(III)**\nFlexible leg openings.\n**(IV)**\nRefastening closures.\n**(12) State**\nThe term State means the 50 States, the District of Columbia, the Commonwealth of Puerto Rico the United States Virgin Islands, Guam, the Commonwealth of the Northern Mariana Islands, American Samoa, the Republic of the Marshall Islands, the Federated States of Micronesia, and the Republic of Palau.\n##### (g) Exemption of program from sequestration\n**(1) In general**\nSection 255(h) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 905(h) ) is amended by inserting after Supplemental Security Income Program (28\u20130406\u20130\u20131\u2013609). the following:\nTargeted funding for States for diaper assistance (including diapering supplies and adult incontinence materials and supplies) through the Social Services Block Grant Program. .\n**(2) Applicability**\nThe amendment made by this subsection shall apply to any sequestration order issued under the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900 et seq. ) on or after the date of enactment of this Act.\n#### 3. Inclusion of diapers and diapering supplies as qualified medical expenses\n##### (a) Health savings accounts\nSection 223(d)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby inserting , medically necessary diapers, and diapering supplies after menstrual care products in the last sentence of subparagraph (A); and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Medically necessary diapers and diapering supplies For purposes of this paragraph\u2014 (i) Medically necessary diapers The term medically necessary diaper means an absorbent garment which is washable or disposable and which is worn by an individual who has attained 3 years of age because of medical necessity, such as someone who has been diagnosed with bowel or bladder incontinence, a bowel or bladder condition that causes excess urine or stool (such as short gut syndrome or diabetes insipidus), or a severe skin condition that causes skin erosions (such as epidermolysis bullosa) and needs such garment to correct or ameliorate such condition, to serve a preventative medical purpose, or to correct or ameliorate defects or physical or mental illnesses or conditions diagnosed by a licensed health care provider, and, if disposable\u2014 (I) does not use any latex or common allergens; and (II) meets or exceeds the quality standards for diapers commercially available through retail sale in the following categories: (aa) Absorbency (with acceptable rates for first and second wetting). (bb) Waterproof outer cover. (cc) Flexible leg openings. (dd) Refastening closures. (ii) Diapering supplies The term diapering supplies means items, including diaper wipes and diaper creams, necessary to ensure that an individual wearing medically necessary diapers is properly cleaned and protected from diaper rash. .\n##### (b) Archer MSAs\nThe last sentence of section 220(d)(2)(A) of such Code is amended by inserting , medically necessary diapers (as defined in section 223(d)(2)(E)), and diapering supplies (as defined in section 223(d)(2)(E)) after menstrual care products (as defined in section 223(d)(2)(D)) .\n##### (c) Health flexible spending arrangements and health reimbursement arrangements\nSection 106(f) of such Code is amended\u2014\n**(1)**\nby inserting , medically necessary diapers (as defined in section 223(d)(2)(E)), and diapering supplies (as defined in section 223(d)(2)(E)) after menstrual care products (as defined in section 223(d)(2)(D)) ; and\n**(2)**\nin the heading, by inserting , medically necessary diapers, and diapering supplies after menstrual care products .\n##### (d) Effective dates\n**(1) Distributions from certain accounts**\nThe amendments made by subsections (a) and (b) shall apply to amounts paid after December 31, 2025.\n**(2) Reimbursements**\nThe amendment made by subsection (c) shall apply to expenses incurred after December 31, 2025.",
      "versionDate": "2025-05-20",
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
        "actionDate": "2025-05-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1815",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "End Diaper Need Act of 2025",
      "type": "S"
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
        "updateDate": "2025-07-11T12:36:07Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3508ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Diaper Need Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-30T05:23:19Z"
    },
    {
      "title": "End Diaper Need Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-30T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide targeted funding for States and other eligible entities through the Social Services Block Grant program to address the increased burden that maintaining the health and hygiene of infants and toddlers, medically complex children, and low-income adults or adults with disabilities who rely on adult incontinence materials and supplies place on families in need, the resultant adverse health effects on children and families, and the limited child care options available for infants and toddlers who lack sufficient diapers and diapering supplies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-30T05:18:18Z"
    }
  ]
}
```
