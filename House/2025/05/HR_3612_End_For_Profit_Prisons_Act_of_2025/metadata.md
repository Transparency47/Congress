# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3612?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3612
- Title: End For-Profit Prisons Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3612
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-06-05T08:06:06Z
- Update date including text: 2025-06-05T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3612",
    "number": "3612",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "End For-Profit Prisons Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-05T08:06:06Z",
    "updateDateIncludingText": "2025-06-05T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:04:15Z",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
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
      "sponsorshipDate": "2025-05-23",
      "state": "NJ"
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
      "sponsorshipDate": "2025-05-23",
      "state": "GA"
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
      "sponsorshipDate": "2025-05-23",
      "state": "IL"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "MA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3612ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3612\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mrs. Watson Coleman (for herself, Ms. Lee of Pennsylvania , Mrs. McIver , Mr. Johnson of Georgia , Mrs. Ramirez , and Mr. McGovern ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo restrict the authority of the Attorney General to enter into contracts for Federal correctional facilities and community confinement facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End For-Profit Prisons Act of 2025 .\n#### 2. Elimination of contracting for Federal correctional facilities and community confinement facilities\n##### (a) In general\nChapter 301 of title 18, United States Code, is amended by adding at the end the following:\n4015. No contracting out of Federal prison facilities or community confinement facilities (a) Federal correctional facilities generally Beginning on the date that is 6 years after the date of the enactment of the End For-Profit Prisons Act of 2025 \u2014 (1) all core correctional services at each correctional facility which is used by the Bureau of Prisons for the confinement of persons serving sentences of imprisonment for Federal offenses shall be performed by employees of the Federal Government; and (2) all core correctional services at each correctional facility which is used by the United States Marshals Service for the confinement of persons in the custody of the United States Marshals Service shall be performed by employees of the Federal Government, except that the United States Marshals Service may enter and maintain a contract with a facility operated by a State or unit of local government if\u2014 (A) the core correctional services at such correctional facility are performed by employees of such State or unit of local government; and (B) the facility meets all constitutional, Federal statutory, United States Marshals Service, and any applicable State or local standards. (b) Federal community confinement facilities Beginning on the date that is 8 years after the date of the enactment of the End For-Profit Prisons Act of 2025 , the Director of the Bureau of Prisons may not enter into or maintain any contract with any for-profit entity to provide or manage any community confinement facility. (c) Definitions In this section: (1) The term community confinement facility has the meaning given that term in section 115.5 of title 28, Code of Federal Regulations (as in effect on the date of the enactment of the End For-Profit Prisons Act of 2025 ). (2) The term core correctional services means the housing, safeguarding, protecting, and disciplining of individuals charged with or convicted of an offense. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 301 of title 18, United States Code, is amended by adding at the end the following new item:\n4015. No contracting out of Federal prison facilities or community confinement facilities. .\n#### 3. Transitional provisions\n##### (a) Federal correctional facilities\nThe Attorney General shall take appropriate action to phase out existing Bureau of Prisons and United States Marshals Service contracts for core correctional services which, at the conclusion of the transition period, will be prohibited under section 4015 of title 18, United States Code.\n##### (b) Federal community confinement facilities\nThe Attorney General shall take appropriate action to phase out existing Bureau of Prisons contracts for community confinement facilities which, at the conclusion of the transition period, will be prohibited under section 4015 of title 18, United States Code.\n#### 4. Report\nNot later than 2 years after the date of the enactment of this Act, and every 2 years thereafter, the Attorney General shall submit to Congress a report which describes and evaluates the prison population in the custody of the Bureau of Prisons. The report shall include information regarding the race, gender, age, and nationality of such persons, as well as the location of the custody of such persons.\n#### 5. Research on programs and policies that reduce recidivism\n##### (a) In general\nThe Attorney General shall conduct research to evaluate the effectiveness at improving community reintegration of programs operated by, and policies of, community confinement facilities (as such term is defined in section 4015 of title 18, United States Code), and shall develop guidelines based on such research for the use of such programs and policies at community confinement facilities.\n##### (b) Report\nNot later than 4 years after the date of the enactment of this Act, and every 4 years thereafter, the Attorney General shall submit to Congress a report which describes the results of the research conducted under subsection (a), the guidelines developed pursuant to such research, and how such guidelines are being incorporated into any contract for the provision or management of a community confinement facility to which the Bureau of Prisons is a party.\n#### 6. Annual inspection of correctional facilities used for the confinement of persons in the custody of the United States Marshals Service\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the United States Marshals Service shall conduct a thorough inspection of each correctional facility which is used by the United States Marshals Service for the confinement of persons in the custody of the United States Marshals Service to ensure that each such facility meets all constitutional, Federal statutory, United States Marshals Service, and any other applicable standards, including any State or local standards.\n#### 7. Duties of the Attorney General relating to the release of Federal Prisoners\nSection 3624 of title 18, United States Code, is amended by adding at the end the following:\n(h) Provision of information and counseling The Attorney General shall make rules to assure that each prisoner released from Federal custody upon the expiration of that prisoner\u2019s term of imprisonment for an offense, including a prisoner who resides in a community confinement facility (as such term is defined in section 4015), receives information and appropriate counseling about each of the following: (1) Any right the prisoner may have to have the prisoner\u2019s criminal record expunged. (2) The availability of programs to remove employment barriers. (3) Relevant vocational and educational rehabilitation programs that are available to the prisoner. (4) A detailed record of participation in educational, employment, and treatment programs completed while incarcerated. (5) Assistance with applications for the following: (A) Programs providing nutritional assistance. (B) Medicaid. (C) Social Security. (D) Driver\u2019s license. (E) Registering to vote. .\n#### 8. Duties of Bureau of Prisons regarding released prisoners\nSection 4042 of title 18, United States Code, is amended by adding at the end the following:\n(e) Requirements with respect to released prisoners In carrying out the duties set forth in subsections (a)(6) and (a)(7), the Director of the Bureau of Prisons shall ensure that each prisoner receives information and counseling during prerelease procedures regarding each area described in subsections (a)(6) and (a)(7). The Director of the Bureau of Prisons shall provide each released prisoner, including a prisoner who resides in a community confinement facility (as such term is defined in section 4015), with information regarding fines, assessments, surcharges, restitution, other penalties due from the prisoner in connection with the conviction, which it shall be the duty of the appropriate judicial officers to provide to the Bureau. .",
      "versionDate": "2025-05-23",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-03T15:39:30Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3612ih.xml"
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
      "title": "End For-Profit Prisons Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End For-Profit Prisons Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restrict the authority of the Attorney General to enter into contracts for Federal correctional facilities and community confinement facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:35Z"
    }
  ]
}
```
