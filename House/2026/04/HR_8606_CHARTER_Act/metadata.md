# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8606
- Title: CHARTER Act
- Congress: 119
- Bill type: HR
- Bill number: 8606
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T13:51:02Z
- Update date including text: 2026-05-20T13:51:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8606",
    "number": "8606",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
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
    "title": "CHARTER Act",
    "type": "HR",
    "updateDate": "2026-05-20T13:51:02Z",
    "updateDateIncludingText": "2026-05-20T13:51:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "AZ"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "KS"
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
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "WA"
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
      "sponsorshipDate": "2026-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8606ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8606\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. DeLauro (for herself, Ms. Bonamici , Mrs. Grijalva , Ms. Castor of Florida , Ms. Davids of Kansas , Mr. Garc\u00eda of Illinois , Ms. Norton , Ms. Jayapal , Ms. Lee of Pennsylvania , Mr. Quigley , Ms. Schakowsky , Ms. Simon , Mr. Takano , Mr. Thanedar , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 and the Individuals with Disabilities Education Act to ensure no funds made available under such Acts may be awarded to a charter school or charter management organization that enters into a contract with a for-profit entity for operating, overseeing, or managing the charter school, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Championing Honest And Responsible Transparency in Education Reform Act or the CHARTER Act .\n#### 2. Purpose and findings\n##### (a) Purpose\nThe purpose of this Act is to ensure that each charter school that receives funding under the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ) (in this section referred to as the ESEA ) or the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ) (in this section referred to as the IDEA )\u2014\n**(1)**\ncomplies with the intent of the requirements for funding under such Act; and\n**(2)**\nbest serves the educational needs of students by prohibiting such charter school and its charter management organization from entering into a contract with a for-profit entity under which the for-profit entity\u2014\n**(A)**\noperates, oversees, or manages the charter school in order to exert influence in school management; and\n**(B)**\nreceives a portion of school revenue in order to extract profit for itself or its related entities.\n##### (b) Findings\nCongress finds the following:\n**(1)**\nAn elementary school is defined as a nonprofit institutional day or residential school, including a public elementary charter school, that provides elementary education, as determined under State law under section 8101 of the ESEA ( 20 U.S.C. 7801 ) and section 602 of the IDEA ( 20 U.S.C. 1401 ).\n**(2)**\nA secondary school is defined as a nonprofit institutional day or residential school, including a public secondary charter school, that provides secondary education, as determined under State law, except that the term does not include any education beyond grade 12 under section 8101 of the ESEA ( 20 U.S.C. 7801 ) and section 602 of the IDEA ( 20 U.S.C. 1401 ).\n**(3)**\nThe term nonprofit as applied to a school, agency, organization, or institution means a school, agency, organization, or institution owned and operated by 1 or more nonprofit corporations or associations no part of the net earnings of which inures, or may lawfully inure, to the benefit of any private shareholder or individual under section 602 of the IDEA ( 20 U.S.C. 1401 ).\n**(4)**\nIn 2003, the Department of Education Office of Inspector General, upon auditing the Arizona Department of Education, concluded that the State educational agency in Arizona had improperly distributed funds under the ESEA and the IDEA to for-profit charter schools.\n**(5)**\nIn 2006, the United States Court of Appeals Ninth Circuit Court in Arizona State Bd. v. U.S. Dept. of Educ., 464 F.3d 1003 (9th Cir. 2006) found that the terms elementary school and secondary school in the ESEA and the IDEA were limited to nonprofit entities, holding that for-profit charter schools were ineligible for Federal funds under the ESEA and the IDEA.\n**(6)**\nIn response to the decision in Arizona State Bd. v. U.S. Dept. of Educ., the appellant for-profit charter schools reorganized as for-profit operators of nonprofit organizations, enabling the appellants to continue to receive Federal funds under the ESEA and the IDEA.\n**(7)**\nEvery student in a publicly funded school in the United States, including charter school students, is entitled to access education services without having publicly funded resources depleted due to profit extraction.\n**(8)**\nEvery taxpayer in the United States should be confident that public funds are responsibly stewarded and not funding the enrichment of for-profit charter operators at the expense of students and taxpayers.\n#### 3. ESEA definition of charter school\n##### (a) Prohibition of contracting with for-Profit entity for essential services\nSection 4310(2) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221i(2) ) is amended\u2014\n**(1)**\nin subparagraph (L), by striking and at the end;\n**(2)**\nin subparagraph (M)\u2014\n**(A)**\nby moving the margins of such paragraph 2 ems to the left; and\n**(B)**\nby striking the period and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(N) does not enter into a contract with a for-profit entity, or have a charter management organization or other nonprofit entity enter into such a contract on behalf of such school, under which the for-profit entity operates, oversees, manages, or otherwise carries out the administration of such school, which may include curriculum development, budget management, and faculty management (such as hiring, terminating, or supervising school-level staff); and (O) may enter into a contract with a for-profit or nonprofit entity for the provision of\u2014 (i) food, payroll, facilities maintenance, or transportation services; (ii) classroom supplies (such as textbooks); or (iii) ancillary services or supplies. .\n##### (b) General definitions\nSection 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ) is amended by adding at the end the following:\n(53) Charter school The term charter school has the meaning given the term in section 4310. .\n#### 4. IDEA definition of charter school\nSection 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 ) is amended by adding at the end the following:\n(37) Charter school The term charter school has the meaning given the term in section 4310 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221i ). .\n#### 5. Effective date; applicability\nThe amendments made by this Act\u2014\n**(1)**\nshall take effect on the date that is 3 years after the date of the enactment of this Act; and\n**(2)**\nshall only apply with respect to any contract entered into, renewed, or extended on or after the date of the enactment of this Act.",
      "versionDate": "2026-04-30",
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
        "name": "Education",
        "updateDate": "2026-05-20T13:51:01Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8606ih.xml"
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
      "title": "CHARTER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHARTER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Championing Honest And Responsible Transparency in Education Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 and the Individuals with Disabilities Education Act to ensure no funds made available under such Acts may be awarded to a charter school or charter management organization that enters into a contract with a for-profit entity for operating, overseeing, or managing the charter school, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:29Z"
    }
  ]
}
```
