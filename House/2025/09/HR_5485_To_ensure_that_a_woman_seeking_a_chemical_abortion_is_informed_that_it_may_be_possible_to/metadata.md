# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5485?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5485
- Title: Second Chance at Life Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5485
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-11-18T17:38:20Z
- Update date including text: 2025-11-18T17:38:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5485",
    "number": "5485",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Second Chance at Life Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-18T17:38:20Z",
    "updateDateIncludingText": "2025-11-18T17:38:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KS"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IN"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "SC"
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
      "sponsorshipDate": "2025-09-18",
      "state": "TN"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "FL"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MS"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MI"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "TN"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "SC"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "OK"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5485ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5485\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Pfluger (for himself, Mr. LaMalfa , Mr. Estes , Mr. Moore of Alabama , Mr. Stutzman , Mrs. Biggs of South Carolina , Mr. Rose , Mrs. Cammack , Mr. McGuire , Mr. Guest , Mr. Finstad , Mr. Weber of Texas , Mr. Goldman of Texas , Mr. Moolenaar , Mr. Crenshaw , and Mr. Bost ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure that a woman seeking a chemical abortion is informed that it may be possible to reverse the intended effects of the abortion if the woman changes her mind, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Second Chance at Life Act of 2025 .\n#### 2. Abortion pill reversal informed consent\nThe Public Health Service Act ( 42 U.S.C. 201 et seq. ) is amended by adding at the end the following:\nXXXIV Abortion pill reversal informed consent 3401. Definitions In this title: (1) Abortion provider The term abortion provider means any person licensed to perform a chemical abortion under applicable Federal and State laws. (2) Chemical abortion The term chemical abortion means the use or prescription of an abortion-inducing drug dispensed with the intent to cause the death of the unborn child. (3) Unborn child The term unborn child means a member of the species homo sapiens, at any stage of development prior to birth. (4) Woman The term woman means a female human being whether or not she has reached the age of majority. 3402. Abortion pill reversal informed consent (a) Requirement of compliance by providers Effective 30 days after the date of enactment of the Second Chance at Life Act of 2025 , any abortion provider in or affecting interstate or foreign commerce, who knowingly performs any chemical abortion, shall comply with the requirements of this title. (b) Informed consent Except in the case of a medical emergency described in section 3403, a chemical abortion involving the two drug process of dispensing mifepristone first and then misoprostol shall not be performed or induced or attempted to be performed or induced without the following: (1) The woman is informed, by telephone or in person, by the physician who is to perform the chemical abortion, by a referring physician, or by an agent of either physician at least 24 hours before the chemical abortion, that\u2014 (A) it may be possible to reverse the intended effects of a mifepristone-induced chemical abortion if the woman changes her mind but that time is of the essence; and (B) information on and assistance with reversing the effects of a mifepristone-induced chemical abortion is available on the website of the Department of Health and Human Services required by section 3405(b). (2) After the first drug involved in the two drug process is dispensed in a mifepristone-induced chemical abortion, the physician shall provide written medical discharge instructions to the pregnant woman which must include the statement: Recent developing research has indicated that mifepristone alone is not always effective in ending a pregnancy. It may be possible to avoid, cease, or even to reverse the intended effects of a mifepristone-induced chemical abortion if the second pill has not been taken. Please consult with a health care professional immediately. . 3403. Exception for medical emergencies (a) Exception The provisions of section 3402 shall not apply in the case where a woman suffers from a physical disorder, physical injury, or physical illness that would, as certified by a physician, place the woman in danger of death unless an abortion is performed, including a life-endangering physical condition caused by or arising from the pregnancy itself. (b) Certification Upon a determination by an abortion provider under subsection (a) that an abortion is necessary to save the life of a mother, such provider shall include in the medical file of the pregnant woman a truthful and accurate certification of the specific medical circumstances that support such determination. 3404. Sign posting (a) Posting Any private office, freestanding surgical outpatient clinic or other facility, or clinic in which chemical abortions, other than abortions necessary in the case of a medical emergency described in section 3403, are performed shall conspicuously post a sign (in a location as described in subsection (c) so as to be clearly visible to patients) which reads: Research has indicated that mifepristone alone is not always effective in ending a pregnancy and that its effects can be blocked or reversed if the second pill has not yet been taken. If you change your mind prior to taking the second pill and desire to attempt to save your pregnancy, consult with a health care professional immediately. . (b) Lettering; size The sign required by subsection (a) shall be printed with lettering that is\u2014 (1) legible; and (2) at least three quarters of an inch boldfaced type. (c) Locations A facility in which chemical abortions are performed that is a private office or a freestanding surgical outpatient clinic shall post the sign required by subsection (a) in each patient waiting room and patient consultation room used by patients on whom chemical abortions are performed. A hospital or any other facility in which chemical abortions are performed that is not a private office or freestanding surgical outpatient clinic shall post the required sign in each patient admission area used by patients on whom chemical abortions are performed. 3405. Printed information and website (a) In general The Secretary shall publish, in English and in each language which is the primary language of 2 percent or more of the population of any State, and shall cause to be available on the website required by subsection (b), the following printed materials in such a way as to ensure that the information is easily comprehensible: (1) Materials designed to inform the woman of the possibility of reversing the effects of a chemical abortion utilizing mifepristone if she changes her mind. (2) Materials on the assistance and resources that may be available to help reverse the effects of a chemical abortion. (b) Website Not later than 30 days after the date of enactment of the Second Chance at Life Act of 2025 , the Secretary shall develop and maintain a website to provide the information described in subsection (a) in accordance with the following: (1) No information regarding who uses the website shall be collected or maintained. (2) The Secretary shall monitor on a regular basis the website to prevent and correct tampering. (3) The website shall be maintained at a minimum resolution of 70 DPI (dots per inch). (4) All pictures appearing on the website shall be a minimum of 200x300 pixels. (5) All letters on the website shall be a minimum of 12 point font. (6) All information and pictures on the website shall be accessible with an industry standard browser, requiring no additional plug-ins. 3406. Civil remedies (a) Civil suits for violation Except as provided in subsection (b), any of the following parties may bring a civil action before the appropriate Federal district court for actual and punitive damages against an abortion provider who knowingly or recklessly performed or attempted to perform a chemical abortion in violation of this title: (1) A person upon whom such a chemical abortion has been performed or attempted. (2) A father of an unborn child who is the subject of such a chemical abortion. (3) A parent of a person upon whom such a chemical abortion has been performed or attempted if such person had not attained 18 years of age at the time of such abortion or if such person died as the result of such abortion. (b) Barring suit A plaintiff may not bring a civil action under subsection (a) if a chemical abortion is performed or attempted with respect to a pregnancy that is the result of the plaintiff\u2019s criminal conduct. (c) Attorney\u2019s fee If a party described in paragraph (1), (2), or (3) of subsection (a) is the prevailing party in an action under this section, the court shall award a reasonable attorney\u2019s fee to such party. If a defendant is the prevailing party in an action under this section, and the court finds that such action was frivolous or brought in bad faith, the court shall award a reasonable attorney\u2019s fee to the defendant. .\n#### 3. Preemption\nNothing in this Act or the amendment made by this Act shall be construed to preempt any provision of State law to the extent that such State law establishes, implements, or continues in effect disclosure requirements regarding abortion or penalties for failure to comply with such requirements that are more extensive than those provided under the amendment made by this Act.\n#### 4. Severability\nIf any provision of this Act, or any application thereof, is found to be unconstitutional, the remainder of this Act and any application thereof shall not be affected by such finding.",
      "versionDate": "2025-09-18",
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
        "name": "Health",
        "updateDate": "2025-11-18T17:38:20Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5485ih.xml"
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
      "title": "Second Chance at Life Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Chance at Life Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that a woman seeking a chemical abortion is informed that it may be possible to reverse the intended effects of the abortion if the woman changes her mind, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:19Z"
    }
  ]
}
```
