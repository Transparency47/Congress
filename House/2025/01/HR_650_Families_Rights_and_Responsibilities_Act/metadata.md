# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/650?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/650
- Title: Families’ Rights and Responsibilities Act
- Congress: 119
- Bill type: HR
- Bill number: 650
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-02-04T05:06:19Z
- Update date including text: 2026-02-04T05:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/650",
    "number": "650",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Families\u2019 Rights and Responsibilities Act",
    "type": "HR",
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
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:01:05Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "LA"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KY"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "SC"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "UT"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NC"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr650ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 650\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Foxx (for herself, Mr. Weber of Texas , Mr. Rose , Mrs. Miller of Illinois , Mr. Bilirakis , Mr. Higgins of Louisiana , Mr. Guthrie , Mr. Finstad , Mr. Loudermilk , Mr. McCormick , and Mr. Haridopolos ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo protect the right of parents to direct the upbringing of their children as a fundamental right.\n#### 1. Short title\nThis Act may be cited as the Families\u2019 Rights and Responsibilities Act .\n#### 2. Congressional findings and declaration of purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe nature of the parent-child relationship endows parents with the primary responsibility and obligation to care for their child.\n**(2)**\nFrom these responsibilities and obligations comes the pre-political, natural right of parents to care for their children.\n**(3)**\nThe role of parents in the raising and rearing of their children is of inestimable value and deserving of both praise and protection by all levels of government.\n**(4)**\nThis right as recognized in the traditions of western civilization recognizes that parents have the responsibility to love, nurture, raise, and protect their children.\n**(5)**\nThe right encompasses the authority of parents to direct the upbringing, education, and health care of their children according to the dictates of their conscience, to direct the upbringing, education, and health care of their children in their own beliefs and religion, and to be the primary decision maker for their child until the child reaches adulthood.\n**(6)**\nThe Supreme Court has consistently recognized the primary role of parents in caring for children, concluding the following:\n**(A)**\n[T]he child is not the mere creature of the state; those who nurture him and direct his destiny have the right, coupled with the high duty, to recognize and prepare him for additional obligations. Pierce v. Soc\u2019y of the Sisters of the Holy Names of Jesus & Mary, 268 U.S. 510, 535 (1925).\n**(B)**\n[I]t is the natural duty of the parent to give his children education suitable to their station in life. Meyer v. Nebraska, 262 U.S. 390, 400 (1923).\n**(C)**\nIt is plain that the interest of a parent in the companionship, care, custody, and management of his or her children comes to this Court with a momentum for respect lacking when appeal is made to liberties which derive merely from shifting economic arrangements. Stanley v. Illinois, 405 U.S. 645, 651 (1972).\n**(D)**\nThe history and culture of Western civilization reflect a strong tradition of parental concern for the nurture and upbringing of their children. This primary role of the parents in the upbringing of their children is now established beyond debate as an enduring American tradition. Wisconsin v. Yoder, 406 U.S. 205, 232 (1972).\n**(E)**\nOur jurisprudence historically has reflected Western civilization concepts of the family as a unit with broad parental authority over minor children. Our cases have consistently followed that course. Parham v. J. R., 442 U.S. 584, 602 (1979).\n**(F)**\nWe have recognized on numerous occasions that the relationship between parent and child is constitutionally protected. Quilloin v. Walcott, 434 U.S. 246, 255 (1978).\n**(G)**\nThe Supreme Court has explained that the liberty specially protected by the Due Process Clause includes the right to direct the education and upbringing of one\u2019s children. Washington v. Glucksberg, 521 U.S. 702, 720 (1997).\n**(H)**\n[W]e have recognized the fundamental right of parents to make decisions concerning the care, custody, and control of their children . . . In light of this extensive precedent, it cannot now be doubted that the Due Process Clause of the Fourteenth Amendment protects the fundamental right of parents to make decisions concerning the care, custody, and control of their children. Troxel v. Granville, 530 U.S. 57, 66 (2000) (plurality op.).\n**(I)**\n[T]he Due Process Clause does not permit a State to infringe on the fundamental right of parents to make child rearing decisions simply because a state judge believes a better decision could be made. Troxel, 530 U.S. at 72\u201373 (plurality op.).\n**(7)**\nSome decisions of Federal courts have failed to recognize the fundamental right of parents, resulting in an improper standard of judicial review being applied to government conduct that adversely affects parental rights and prerogatives.\n**(8)**\nGovernment agencies have increasingly intruded into the legitimate decisions and prerogatives of parents in situations that do not involve abuse or neglect but simply an agency\u2019s disagreement with parenting choices based on decent and honorable religious or philosophical premises.\n**(9)**\nGovernment\u2019s involvement in parenting should prioritize the parent\u2019s role as the child\u2019s primary educator and should support, not supplant, the parent\u2019s rights and responsibilities.\n**(10)**\nGovernment should not interfere in the decisions and actions of parents without compelling justification.\n**(11)**\nThe strict scrutiny test used by courts to evaluate cases concerning fundamental rights is the correct standard of review for government actions that interfere with the right of parents to direct the upbringing, education, and health care of their children, and it appropriately balances the interests of parents, children, and government.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto protect the right of parents to direct the upbringing of their children as a fundamental right; and\n**(2)**\nwhile protecting the right of parents, to acknowledge that the rights involve responsibilities and specifically that parents have the responsibility for the education, nurture, and upbringing of their children as specified by the Supreme Court in Meyer v. Nebraska, 262 U.S. 390, 400 (1923), Wisconsin v. Yoder, 406 U.S. 205, 232 (1972), and Washington v. Glucksberg, 521 U.S. 702, 720 (1997), and have the high duty to recognize and prepare their children for additional obligations as specified by the Supreme Court in Pierce v. Soc\u2019y of the Sisters of the Holy Names of Jesus & Mary, 268 U.S. 510, 535 (1925).\n#### 3. Definitions\nIn this Act:\n**(1) Government**\nThe term government includes a branch, department, agency, instrumentality, and official (or other person acting under color of law) of the United States, the District of Columbia, the Commonwealth of Puerto Rico, and each territory and possession of the United States.\n**(2) Parent**\nThe term parent means a biological parent of a child, an adoptive parent of a child, or an individual who has been granted exclusive right and authority over the welfare of a child under State law.\n**(3) Child**\nThe term child means an individual who has not attained 18 years of age.\n**(4) Substantial burden**\nThe term substantial burden \u2014\n**(A)**\nmeans any action that directly or indirectly constrains, inhibits, curtails, or denies the right of parents to direct the upbringing, education, and health care of their child or compels any action contrary to the right of parents to direct the upbringing, education, and health care of their child; and\n**(B)**\nincludes withholding benefits, assessing criminal, civil, or administrative penalties or damages, or exclusion from governmental programs.\n#### 4. Protection of parental rights\n##### (a) In general\n**(1) Fundamental right**\nThe liberty of parents to direct the upbringing, education, and health care of their children is a fundamental right.\n**(2) Limits on government interference**\nGovernment shall not substantially burden the fundamental right of parents to direct the upbringing, education, and health care of their children without demonstrating that the infringement is required by a compelling governmental interest of the highest order as applied to the parent and the child and is the least restrictive means of furthering that compelling governmental interest. The fundamental rights protected include, without limitation, the following rights and responsibilities:\n**(A)**\nTo direct the education of the child.\n**(B)**\nTo direct the moral or religious upbringing of the child.\n**(C)**\nTo access and review all medical records of the child and to make and consent to all physical and mental health care decisions for the child.\n**(3) Effect of this Act on other rights**\nUnless legally waived or legally terminated, parents have inalienable rights that are more comprehensive than those listed in this section. This Act does not prescribe all rights of parents, nor does it preempt or foreclose claims or remedies in support of parental rights that are available under any other Federal law, State law, the United States Constitution, or a State constitution.\n##### (b) Exceptions\nThis section does not apply to a parental action or decision that would result in serious physical injury to the child or that would end life.\n##### (c) Judicial remedy\nAny parent may raise a violation of this Act as a claim or a defense in an action in a Federal or State court or before an administrative tribunal and obtain appropriate relief against a government. Standing to assert a claim or defense under this section shall be governed by the general rules of standing under article III of the Constitution.\n#### 5. Attorneys fees\n##### (a) Judicial Proceedings\nSection 722(b) of the Revised Statutes ( 42 U.S.C. 1988(b) ) is amended by inserting the Families\u2019 Rights and Responsibilities Act, before title VI of the Civil Rights Act of 1964 .\n##### (b) Administrative Proceedings\nSection 504(b)(1)(C) of title 5, United States Code, is amended by striking the Religious Freedom Restoration Act of 1993 and inserting any adjudication under the Religious Freedom Restoration Act of 1993 or the Families\u2019 Rights and Responsibilities Act .\n#### 6. Applicability\n##### (a) In General\nThis Act applies to each Federal law, and the implementation of any such law, whether statutory or otherwise, and whether adopted before or after the date of enactment of this Act.\n##### (b) Rule of construction\n**(1) Additional rights**\nThe protections of the fundamental right of parents to direct the upbringing, education, and health care of their children afforded by this Act are in addition to the protections provided under Federal law, State law, and the State and Federal constitutions.\n**(2) Broad protection**\nThis Act shall be construed in favor of a broad protection of the fundamental right of parents to direct the upbringing, education, and health care of their children.\n**(3) No government burden**\nNothing in this Act shall be construed to authorize any government to burden the fundamental right of parents to direct the upbringing, education, and health care of their children.\n**(4) Subsequently enacted laws**\nFederal statutory law adopted after the date of the enactment of this Act is subject to this Act, unless such law explicitly excludes such application by reference to this Act.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "204",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Families\u2019 Rights and Responsibilities Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child care and development",
            "updateDate": "2025-03-17T15:51:36Z"
          },
          {
            "name": "Child health",
            "updateDate": "2025-03-17T15:54:23Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-17T15:54:32Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-17T15:54:11Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-03-17T15:54:04Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-17T15:54:17Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-03-17T15:54:37Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-03-17T15:54:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-02-24T19:31:15Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr650ih.xml"
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
      "title": "Families\u2019 Rights and Responsibilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Families\u2019 Rights and Responsibilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect the right of parents to direct the upbringing of their children as a fundamental right.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:41Z"
    }
  ]
}
```
