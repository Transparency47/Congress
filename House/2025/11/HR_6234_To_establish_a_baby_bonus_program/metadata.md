# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6234
- Title: Baby Bonus Act
- Congress: 119
- Bill type: HR
- Bill number: 6234
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-13T09:05:39Z
- Update date including text: 2026-01-13T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6234",
    "number": "6234",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
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
    "title": "Baby Bonus Act",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:39Z",
    "updateDateIncludingText": "2026-01-13T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:01:30Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DC"
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
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CO"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-11-28",
      "state": "MD"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6234ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6234\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Tlaib (for herself, Ms. Norton , Ms. Lee of Pennsylvania , Mrs. McIver , Ms. Omar , Mr. Thanedar , Mrs. Watson Coleman , Ms. Pressley , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo establish a baby bonus program.\n#### 1. Short title\nThis Act may be cited as the Baby Bonus Act .\n#### 2. Establishment of the office of baby assistance\n##### (a) In general\nThere is established within the Social Security Administration an office to be known as the Office of Baby Assistance. The Office shall be headed by a Deputy Commissioner appointed by the Commissioner of Social Security.\n##### (b) Responsibilities of deputy commissioner\nThe Commissioner, acting through the Deputy Commissioner, shall\u2014\n**(1)**\nhire such personnel as are necessary for the Office of Baby Assistance and make employment decisions with regard to such personnel;\n**(2)**\nhave the authority to enter into contracts or cooperative agreements with other agencies and departments as are necessary to ensure the efficiency of the program;\n**(3)**\nmake baby bonus payments to eligible parents pursuant to section 3 ;\n**(4)**\nreview applications for baby bonus payments;\n**(5)**\nestablish and maintain a system of records relating to the administration of this Act;\n**(6)**\nprevent fraud and abuse relating to baby bonus payments;\n**(7)**\nprovide information to the public in relation to baby bonus payments, including eligibility requirements, the application process, payment amounts, and limitations on payments;\n**(8)**\ntailor culturally and linguistically competent education and outreach toward increasing utilization rates of baby bonus payments;\n**(9)**\nissue an annual report to Congress detailing the effect of baby bonus payments, including\u2014\n**(A)**\nthe number of individuals receiving payments;\n**(B)**\nthe total amount of funds disbursed;\n**(C)**\ndemographic data of individuals receiving payments; and\n**(D)**\nsuch other information as the Deputy Commissioner determines is necessary; and\n**(10)**\nissue such regulations as are necessary to carry out this Act.\n##### (c) Availability of data\nThe Commissioner shall make available to the Deputy Commissioner such data as the Commissioner determines necessary to enable the Deputy Commissioner to effectively carry out the responsibilities described in subsection (b) .\n#### 3. Baby bonus payments\n##### (a) Baby bonus\n**(1) In general**\nBeginning January 1st, 2026, and subject to paragraph (2), the Commissioner shall pay, in relation to each qualifying child, a baby bonus to one or more eligible parents of such child in accordance with this section. In the case of multiple qualifying children from a single pregnancy, a separate payment shall be made for each qualifying child.\n**(2) Application required**\nIn order to receive a payment under this section, an eligible parent (or an authorized representative described in subsection (c)(5) ) of a qualifying child shall submit an application in accordance with subsection (c) . Such application shall be submitted not later than 1 year after\u2014\n**(A)**\nthe birth of the qualifying child in relation to which such application is submitted; or\n**(B)**\nin the case of the death of a fetus or qualifying child as described in subsection (e), the date of such death.\n**(3) Amount**\n**(A) In general**\nThe amount of a baby bonus shall be\u2014\n**(i)**\nfor calendar year 2026, $2,000; and\n**(ii)**\nfor any calendar year after such year\u2014\n**(I)**\nthe amount in clause (i) , multiplied by\n**(II)**\nthe cost-of-living adjustment determined under section 1(f)(3) of the Internal Revenue Code of 1986 for the calendar year in which the taxable year begins, determined by substituting 2026 for 2016 in subparagraph (A)(ii) thereof.\n**(B) Rounding**\nIf any amount determined under subparagraph (A) is not a multiple of $1, such increase shall be rounded to the next lower multiple of $1.\n##### (b) Payment\n**(1) Date of payment**\nPayment shall be made\u2014\n**(A)**\nif no objection is made as described in paragraph (3)(A) , during the 6-business day period immediately following the 21-day period beginning on the date on which notice is provided pursuant to such paragraph;\n**(B)**\nif such an objection is raised, during the 6-business day period following the date on which the Commissioner determines which eligible parent is entitled to such money; or\n**(C)**\nif the Commissioner determines pursuant to paragraph (3)(A) that notice is not necessary, during the 10-business day period beginning on the date on which the application is approved under subsection (c)(1).\n**(2) Advanced payment**\nAn eligible parent who has an approved application under subsection (c)(2) is eligible to receive a baby bonus up to 60 days before the expected due date.\n**(3) Consideration of custody**\n**(A) Notice requirement**\nThe Commissioner shall provide notice to all known eligible parents when an application for child payments is approved under subsection (c)(1) providing 21 days for any objections before payment is made. Notwithstanding the prior sentence, the Commissioner may elect not to provide such notice if the Commissioner determines that the applicant has produced clear evidence that providing such notice will not result in an individual other than the eligible parent receiving the baby bonus payment.\n**(B) Child payments**\nWhere multiple eligible parents submit applications for the same qualifying child, payment shall be made to the eligible parent who\u2014\n**(i)**\nhas primary or sole physical custody, as evidenced by a court order;\n**(ii)**\nthe child primarily resides with, in the absence of such a court order; or\n**(iii)**\nif neither clause (i) or (ii) can be determined, the first approved applicant.\n**(C) Joint custody exception**\nNotwithstanding subparagraph (B) , where parents have a court order establishing equal shared physical custody, either parent may request that the payment be divided equally. The Commissioner shall so divide the payment unless the other parent declines, in writing, their share of the payment within 21 days of notification.\n**(D) Dispute resolution**\nIn cases in which a dispute exists as to which eligible parent should receive the payment pursuant to subparagraph (B) and there is no applicable court order, the Commissioner may require submission of such additional documentation as the Commissioner determines appropriate before making payment.\n**(E) Changed circumstances**\nNotwithstanding subsection (a)(1) , the Commissioner may transfer payment to a different eligible parent (or if payment has already been made, may issue payment to a different eligible parent and attempt to recover the original payment in accordance with subsection (e) ) upon receiving documentation showing that\u2014\n**(i)**\nduring the 1-year period beginning on the date on which the child is born\u2014\n**(I)**\ncustody arrangements were modified by court order subsequent to the initial application; or\n**(II)**\nthe original recipient died or became legally incapacitated;\n**(ii)**\nthe original application contained fraudulent information; and\n**(iii)**\nin the case of payment made to a prospective adoptive parent described in section 4(4)(C)(ii)(II) , the adoption is not completed within 60 days of the birth of the qualifying child.\n##### (c) Application\n**(1) Approval process**\nNot later than 14 days after the receipt of an application, the Commissioner shall verify that the applicant meets the requirements established under this section. The application of any applicant so verified shall be considered approved.\n**(2) Application**\nSubject to paragraph (3) , an eligible parent (or an authorized representative described in paragraph (5) ) applying for a baby bonus payment shall provide the Commissioner with an application in such form and manner as the Commissioner may require. The application shall include\u2014\n**(A)**\nthe name and social security account number or taxpayer identification number of the eligible parent;\n**(B)**\n**(i)**\nif the eligible parent is applying before birth of the child, verification of gestational age obtained under paragraph (4) ; or\n**(ii)**\nif the eligible parent is applying after the birth of the child, documentation determined appropriate by the Commissioner to prove the age and identity of the child;\n**(C)**\na written statement from the gestational parent stating, under penalty of perjury pursuant to section 1746 of title 28, United States Code\u2014\n**(i)**\nwhether such person is the biological parent of such fetus; and\n**(ii)**\nwhether such person\u2014\n**(I)**\nintends to retain custody of and parental rights to such child once born;\n**(II)**\nis acting as a gestational surrogate pursuant to a written surrogacy agreement and consents to the intended parent receiving the baby bonus payment; or\n**(III)**\nhas entered into a pre-birth adoption agreement and consents to the prospective adoptive parent receiving the baby bonus payment;\n**(D)**\nthe contact information of any other eligible parent known to the applicant; and\n**(E)**\nsuch other information as the Commissioner determines necessary.\n**(3) Simultaneous application**\nIf an eligible parent has not received a baby bonus and does not have an application under paragraph (2) , the Commissioner shall treat an application for a social security account number for a qualifying child as an application for a baby bonus payment under this section unless the eligible parent affirmatively indicates on such social security account number application an intent to opt out of receiving a baby bonus. The Commissioner may require, as a condition of receiving a payment under subsection (a) , that the eligible parent submit information required under paragraph (2) in addition to the application for a social security account number.\n**(4) Verification of gestational age**\n**(A) In general**\nUpon the request of a gestational parent, a physician may make a determination with respect to the gestational age and expected due date of the fetus. Any determination made under this paragraph shall be based on the reasonable medical judgment of the physician following such inquiries, examinations, and tests as a reasonably prudent physician would deem necessary for purposes of making such determination.\n**(B) Form**\nIf the physician has made a determination pursuant to subparagraph (A) that the gestational age of the fetus is 20 weeks or greater and the expected due date is on or after January 1st, 2026, such physician shall, upon the request of the gestational parent, provide the gestational parent with a form which includes the following:\n**(i)**\nThe gestational age and the expected due date of the fetus.\n**(ii)**\nThe name and social security account number or taxpayer identification number of the gestational parent.\n**(iii)**\nIf the application is being submitted by a spouse or domestic partner of a gestational parent, the name and social security account number or taxpayer identification number of such spouse or domestic partner.\n**(iv)**\nThe name and contact information of the physician.\n**(v)**\nA written documentation from such physician stating, under penalty of perjury pursuant to section 1746 of title 28, United States Code, that\u2014\n**(I)**\nthe gestational parent was determined to be pregnant with the fetus, according to standard medical practice, by such physician; and\n**(II)**\nsuch physician has determined that, in their reasonable medical judgment, the gestational age of the fetus is 20 weeks or greater and the expected due date is on or after January 1st, 2026.\n**(5) Authorized representatives**\n**(A) In general**\nAn application may be submitted on behalf of an eligible parent by\u2014\n**(i)**\na spouse or domestic partner;\n**(ii)**\na legal representative;\n**(iii)**\na healthcare provider involved in providing prenatal or postnatal care to the eligible parent; or\n**(iv)**\nan social service agency determined appropriate by the Commissioner to submit such applications.\n**(B) Documentation**\nThe Commissioner may require that a person submitting a request in accordance with subparagraph (A) provide such documentation as the Commissioner determines appropriate to prevent fraud or abuse.\n##### (d) Effect of death or loss of qualifying child\nIn the case of the involuntary death of a fetus or qualifying child, or the death of a fetus or qualifying child as a result of any treatment intended to save the life of the gestational parent or any treatment of an ectopic pregnancy, occurring after 20 weeks gestation, such death shall have no effect with respect to whether the payment is allowed under this section to an eligible parent, provided that such person otherwise satisfies the applicable requirements under this section.\n##### (e) Payment recovery; penalties\n**(1) Overpayments and underpayment**\n**(A) In general**\nWhenever the Commissioner determines that more or less than the correct amount of payment has been made to a person, proper adjustment or recovery shall be made in the same manner as adjustment or recovery is made under section 204 of the Social Security Act ( 42 U.S.C. 404 ) with respect to overpayments or underpayments under title II of such Act. Notwithstanding the previous sentence, payments under such title may not be adjusted for the purpose of recovering a payment under this section.\n**(B) Other recovery**\nIn the case of an overpayment to an individual who later becomes entitled to a benefit under this section, the Commissioner may decrease such benefit in order to recover such overpayment.\n**(2) Penalties**\nSection 208 of the Social Security Act ( 42 U.S.C. 408 ) shall apply with respect to baby bonus payments under this section in the same manner as such section applies with respect to monthly insurance benefits under title II of such Act.\n##### (f) Income disregard\nA baby bonus payment made under this section shall not be taken into account as income for purposes of the Internal Revenue Code of 1986, and shall not be taken into account as income or resources for purposes of determining the eligibility of such individual or any other individual for benefits or assistance, or the amount or extent of benefits or assistance, under any Federal program or under any State or local program financed in whole or in part with Federal funds.\n##### (g) Prohibition\nNotwithstanding any other provision of law, information submitted pursuant to subsection (c) may not be used for any purpose other than to determine eligibility for a baby bonus payment under this section.\n#### 4. Definitions\nIn this section:\n**(1) Business day**\nThe term business day means any day other than Saturday, Sunday, or a legal public holiday described in section 6103 of title 5, United States Code.\n**(2) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(3) Deputy commissioner**\nThe term Deputy Commissioner means the Deputy Commissioner of the Office of Baby Assistance established under section 2(a) .\n**(4) Eligible parent**\nThe term eligible parent means an individual (other than an ineligible person) who\u2014\n**(A)**\nresides in the United States;\n**(B)**\nis\u2014\n**(i)**\na citizen or national of the United States; or\n**(ii)**\na qualified alien (as defined in section 431 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1641 )); and\n**(C)**\nis\u2014\n**(i)**\nthe parent (other than an ineligible person) or legal guardian of a qualifying child; or\n**(ii)**\nif the parent is an ineligible person\u2014\n**(I)**\nan intended parent in a surrogacy arrangement; or\n**(II)**\na prospective adoptive parent with a court-approved pre-birth adoption agreement\n**(5) Fetus**\nThe term fetus means a human fetus and includes an embryo.\n**(6) Gestational age**\nThe term gestational age means the age of a fetus, as calculated from the first day of the pregnant person\u2019s last menstrual period.\n**(7) Gestational parent**\nThe term gestational parent means an individual who is or was pregnant with a qualifying child, including an individual who is an ineligible person.\n**(8) Ineligible person**\nThe term ineligible person means\u2014\n**(A)**\na gestational parent who\u2014\n**(i)**\nenters into a court-approved pre-birth adoption agreement with an adoptive parent; and\n**(ii)**\ncompletes the adoption process for the child within 60 days of birth; or\n**(B)**\na surrogate who has a surrogacy arrangement in a State that recognizes the intended parent\u2019s legal rights to the qualifying child upon birth.\n**(9) Physician**\nThe term physician means an individual who is\u2014\n**(A)**\nlicensed by a State or territory of the United States to practice\u2014\n**(i)**\nmedicine and surgery;\n**(ii)**\nosteopathic medicine and surgery; or\n**(iii)**\nmidwifery; or\n**(B)**\notherwise legally authorized to\u2014\n**(i)**\nperform births and to diagnose and attend miscarriages or stillbirths; and\n**(ii)**\nperform examinations to determine the gestational age of a fetus by the State in which such practice is performed.\n**(10) Qualifying child**\nThe term qualifying child means\u2014\n**(A)**\na child born on or after January 1st, 2026; or\n**(B)**\na fetus with a gestational age of at least 20 weeks and an expected due date on or after January 1st, 2026, as certified by a physician.\n**(11) Surrogate**\nThe term surrogate means an individual who carries a fetus conceived through assisted reproductive technology and who has entered into a surrogacy arrangement.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-12-18T17:00:03Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6234ih.xml"
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
      "title": "Baby Bonus Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T07:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Baby Bonus Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a baby bonus program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T07:33:35Z"
    }
  ]
}
```
