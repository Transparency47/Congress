# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2302
- Title: Access to Birth Control Act
- Congress: 119
- Bill type: S
- Bill number: 2302
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2026-01-29T12:03:18Z
- Update date including text: 2026-01-29T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-08-01 - Floor: Star Print ordered on the bill.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-08-01 - Floor: Star Print ordered on the bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2302",
    "number": "2302",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Access to Birth Control Act",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T15:54:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "WA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NH"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "WI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NV"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "RI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NM"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MN"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
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
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OR"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MD"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MD"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2302is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2302\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Booker (for himself, Mrs. Murray , Mrs. Shaheen , Ms. Baldwin , Mr. Kaine , Mr. Blumenthal , Ms. Duckworth , Mrs. Gillibrand , Mr. Warner , Ms. Rosen , Mr. Whitehouse , Mr. Heinrich , Ms. Smith , Ms. Hirono , Mr. Schiff , Ms. Warren , Mr. Wyden , Mr. Markey , Mr. Merkley , Mr. Van Hollen , Ms. Alsobrooks , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to establish certain duties for pharmacies to ensure provision of Food and Drug Administration-approved contraception and medication related to contraception, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Birth Control Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nFamily planning is basic health care. Access to contraception helps people determine if and when to become pregnant. Contraception is also a cornerstone of reproductive autonomy and can help people fulfill their educational, professional, and social aspirations.\n**(2)**\nAs a result of the enactment of the Patient Protection and Affordable Care Act ( Public Law 111\u2013148 ), approximately 151,600,000 individuals in the United States were enrolled in private health insurance plans in the United States in 2020, including 58,000,000 women between the ages of 19 and 64 who had coverage of contraceptive methods approved, cleared, or authorized by the Food and Drug Administration without cost-sharing under such plans.\n**(3)**\nThe Patient Protection and Affordable Care Act saved women $1,400,000,000 on birth control pills alone in 2013.\n**(4)**\nAccording to the Centers for Disease Control and Prevention, nearly 2/3 of women between the ages of 15 and 49 are currently using a contraceptive method, and among sexually active women who were not seeking pregnancy, nearly 9 in 10 have used contraception.\n**(5)**\nAlthough the Centers for Disease Control and Prevention included family planning in its published list of the Ten Great Public Health Achievements in the 20th Century, people in the United States face a myriad of barriers in accessing birth control, including cost, geography, immigration status, language access, discrimination, and stigma. These contraceptive barriers are rooted in systemic inequities, structural racism, and other forms of oppression in our health care system and society.\n**(6)**\nIn 2019, approximately 2,293,000 pregnancies, nearly 42 percent of all pregnancies, in the United States were unintended.\n**(7)**\nSystemic racism and discrimination, as well as lack of access to comprehensive sex education, exacerbates severe health inequities and creates additional barriers to accessing contraception; for example, due to high uninsured rates and barriers, Hispanic women with low-incomes experience a significantly higher rate of unintended pregnancy (58 percent) compared to their White counterparts (33 percent). In a 2023 study exploring challenges accessing contraceptive care among people who identified as Asian American, Native Hawaiian, or Pacific Islander, Black or African American, Indigenous, or Latina/Latinx, 45 percent of respondents reported experiencing at least one challenge accessing contraception in the past year.\n**(8)**\nIn addition to preventing pregnancy, contraceptives are used for a range of medical purposes, such as treating abnormal uterine bleeding, irregular menstrual cycles, and endometriosis, as well as for people managing other chronic conditions, which are generally higher in communities of color due to systemic discrimination.\n**(9)**\nThe Food and Drug Administration has approved, cleared, or authorized multiple emergency contraceptive methods as safe and effective in preventing unintended pregnancy and has approved over-the-counter access to some forms of emergency contraception for all individuals, regardless of age. If taken soon after unprotected sex or primary contraceptive failure, emergency contraception can significantly reduce a person\u2019s chance of unintended pregnancy. Additionally, in 2023, the Food and Drug Administration approved the first over-the-counter daily birth control pill which will give people of all ages greater access to birth control options without a prescription.\n**(10)**\nContraception is a protected fundamental right in the United States and access to contraception should not be impeded by one individual\u2019s personal beliefs. Providers, including pharmacists, play a key role in providing contraceptive services and important information about prescription and over-the-counter birth control options to people across the country. It is critical that contraceptive care is provided to people of all ages in a supportive way that is culturally appropriate and delivered without stigma, bias, or delay.\n**(11)**\nReports of pharmacists refusing to fill prescriptions for contraceptives, including emergency contraceptives, or provide emergency contraception over-the-counter have surfaced in States across the Nation, including Alabama, Arizona, California, the District of Columbia, Georgia, Illinois, Louisiana, Massachusetts, Michigan, Minnesota, Missouri, Montana, New Hampshire, New Mexico, New York, North Carolina, Ohio, Oklahoma, Oregon, Rhode Island, Tennessee, Texas, Washington, West Virginia, and Wisconsin.\n**(12)**\nSince the Supreme Court decision in Dobbs v. Jackson Women\u2019s Health Organization (142 S. Ct. 2228 (2022)), there have been increased reports of people being denied birth control at pharmacies.\n**(13)**\nIn 2022, the Department of Health and Human Services issued guidance clarifying that refusing to dispense birth control can be sex discrimination under section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18116 ).\n#### 3. Duties of pharmacies to ensure provision of contraception and medication related to contraception\nPart B of title II of the Public Health Service Act ( 42 U.S.C. 238 et seq. ) is amended by adding at the end the following:\n249. Duties of pharmacies to ensure provision of contraception and medication related to contraception (a) In General Subject to subsection (c), a pharmacy that receives drugs or devices approved, cleared, or authorized by the Food and Drug Administration in interstate commerce shall maintain compliance with the following: (1) If a customer requests a contraceptive or a medication related to a contraceptive that is in stock, the pharmacy shall ensure that the contraceptive or the medication related to a contraceptive is provided to the customer without delay. (2) If a customer requests a contraceptive or a medication related to a contraceptive that is not in stock and the pharmacy in the normal course of business stocks contraception or the medication related to contraception, the pharmacy shall immediately inform the customer that the contraceptive or the medication related to a contraceptive is not in stock and without delay offer the customer the following options: (A) If the customer prefers to obtain the contraceptive or the medication related to a contraceptive through a referral or transfer, the pharmacy shall\u2014 (i) locate a pharmacy of the customer\u2019s choice or the closest pharmacy confirmed to have the contraceptive or the medication related to a contraceptive in stock; and (ii) refer the customer or transfer the prescription to that pharmacy. (B) If the customer prefers for the pharmacy to order the contraceptive or the medication related to a contraceptive, the pharmacy shall obtain the contraceptive or the medication related to a contraceptive under the pharmacy\u2019s standard procedure for expedited ordering of medication and notify the customer when the contraceptive or the medication related to a contraceptive arrives. (3) The pharmacy shall ensure that\u2014 (A) it does not operate an environment in which customers are intimidated, threatened, or harassed in the delivery of services relating to a request for contraception or a medication related to contraception; (B) its employees do not interfere with or obstruct the delivery of services relating to a request for contraception or a medication related to contraception; (C) its employees do not intentionally misrepresent or deceive customers about the availability of contraception or a medication related to contraception or its mechanism of action; (D) its employees do not breach medical confidentiality with respect to a request for contraception or a medication related to contraception or threaten to breach such confidentiality; or (E) its employees do not refuse to return a valid, lawful prescription for contraception or a medication related to contraception upon customer request. (b) Contraceptives or medication related to a contraceptive not ordinarily stocked Nothing in subsection (a)(2) shall be construed to require any pharmacy to comply with such subsection if the pharmacy does not ordinarily stock contraceptives or medication related to a contraceptive in the normal course of business. (c) Refusals Pursuant to Standard Pharmacy Practice This section does not prohibit a pharmacy from refusing to provide a contraceptive or a medication related to a contraceptive to a customer in accordance with any of the following: (1) If it is unlawful to dispense the contraceptive or the medication related to a contraceptive to the customer without a valid, lawful prescription and no such prescription is presented. (2) If the customer is unable to pay for the contraceptive or the medication related to a contraceptive. (3) If the employee of the pharmacy refuses to provide the contraceptive or the medication related to a contraceptive on the basis of a professional clinical judgment. (d) Relation to other laws (1) Rule of construction Nothing in this section shall be construed to invalidate or limit rights, remedies, procedures, or legal standards under title VII of the Civil Rights Act of 1964. (2) Certain claims The Religious Freedom Restoration Act of 1993 shall not provide a claim concerning, or a defense to a claim under, a covered title, or provide a basis for challenging the application or enforcement of a covered title. (e) Preemption This section does not preempt any provision of State law or any professional obligation made applicable by a State board or other entity responsible for licensing or discipline of pharmacies or pharmacists, to the extent that such State law or professional obligation provides protections for customers that are greater than the protections provided by this section. (f) Enforcement (1) Civil penalty A pharmacy that violates a requirement of subsection (a) is liable to the United States for a civil penalty in an amount not exceeding $1,000 per day of violation, not to exceed $100,000 for all violations adjudicated in a single proceeding. (2) Private cause of action Any person aggrieved as a result of a violation of a requirement of subsection (a) may, in any court of competent jurisdiction, commence a civil action against the pharmacy involved to obtain appropriate relief, including actual and punitive damages, injunctive relief, and a reasonable attorney\u2019s fee and cost. (3) Limitations A civil action under paragraph (1) or (2) may not be commenced against a pharmacy after the expiration of the 5-year period beginning on the date on which the pharmacy allegedly engaged in the violation involved. (g) Definitions In this section: (1) The term contraception or contraceptive means any drug or device approved, cleared, or authorized by the Food and Drug Administration to prevent pregnancy. (2) The term employee means a person hired, by contract or any other form of an agreement, by a pharmacy. (3) The term medication related to contraception or medication related to a contraceptive means any drug or device approved, cleared, or authorized by the Food and Drug Administration that a medical professional determines necessary to use before or in conjunction with contraception or a contraceptive. (4) The term pharmacy means an entity that\u2014 (A) is authorized by a State to engage in the business of selling prescription drugs at retail; and (B) employs one or more employees. (5) The term product means a drug or device approved, cleared, or authorized by the Food and Drug Administration. (6) The term professional clinical judgment means the use of professional knowledge and skills to form a clinical judgment, in accordance with prevailing medical standards. (7) The term without delay , with respect to a pharmacy providing, providing a referral for, or ordering contraception or a medication related to contraception, or transferring the prescription for contraception or a medication related to contraception, means within the usual and customary timeframe at the pharmacy for providing, providing a referral for, or ordering other products, or transferring the prescription for other products, respectively. (h) Effective Date This section shall take effect 31 days after the date of enactment of this section, without regard to whether the Secretary has issued any guidance or final rule regarding this section. .",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-06-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4084",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Access to Birth Control Act",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-09-23T19:01:20Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-09-23T19:01:11Z"
          },
          {
            "name": "Family planning and birth control",
            "updateDate": "2025-09-23T19:01:07Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-09-23T19:01:54Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-09-23T19:01:24Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-09-23T19:01:28Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-09-23T19:01:15Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-09-23T19:01:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-23T16:10:44Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2302is.xml"
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
      "title": "Access to Birth Control Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Birth Control Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to establish certain duties for pharmacies to ensure provision of Food and Drug Administration-approved contraception and medication related to contraception, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:29Z"
    }
  ]
}
```
