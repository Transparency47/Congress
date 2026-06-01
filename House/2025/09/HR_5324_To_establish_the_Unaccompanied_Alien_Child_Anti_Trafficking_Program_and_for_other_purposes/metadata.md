# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5324
- Title: No More Missing Children Act
- Congress: 119
- Bill type: HR
- Bill number: 5324
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-24T15:02:57Z
- Update date including text: 2025-09-24T15:02:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5324",
    "number": "5324",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "No More Missing Children Act",
    "type": "HR",
    "updateDate": "2025-09-24T15:02:57Z",
    "updateDateIncludingText": "2025-09-24T15:02:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:01:40Z",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "TN"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5324ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5324\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Ms. Mace (for herself, Mr. Burchett , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish the Unaccompanied Alien Child Anti-Trafficking Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No More Missing Children Act .\n#### 2. Unaccompanied alien child anti-trafficking program\n##### (a) Establishment\nThe Secretary of Health and Human Services (referred to in this Act as the Secretary ), in coordination with the Secretary of Homeland Security, shall establish a program to be known as the Unaccompanied Alien Child Anti-Trafficking Program (referred to in this Act as the Program ) to prevent the trafficking, disappearance, or loss of unaccompanied alien children.\n##### (b) Enrollment\n**(1) In general**\nThe Secretary shall enroll in the Program\u2014\n**(A)**\neach unaccompanied alien child released from the custody of the Secretary on or after the date of enactment of this Act; and\n**(B)**\neach unaccompanied alien child released from the custody of the Secretary before the date of enactment of this Act who is physically present in the United States as of such date of enactment.\n**(2) Duration**\nEach unaccompanied alien child enrolled in the Program shall remain so enrolled until the earliest of\u2014\n**(A)**\nthe removal of the child, if ordered removed;\n**(B)**\nthe date on which the child attains the age of 18; or\n**(C)**\nthe child obtains lawful status under the immigration laws.\n##### (c) Duties of the Secretary\nIn carrying out the Program, the Secretary shall do the following:\n**(1)**\nEnsure that any sponsor to whom an unaccompanied alien child is released under section 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 ) is vetted in accordance with subsection (d), and is not ineligible to serve as a sponsor under subsection (e).\n**(2)**\nRequire each unaccompanied alien child and each sponsor of such child to be continuously monitored by GPS for the duration of the period that the child resides with the sponsor.\n**(3)**\nIn the case of an unaccompanied alien child who has attained the age of 4, require telephonic reporting for both the sponsor and the child, not less than once per month.\n**(4)**\nCollect the DNA of each unaccompanied alien child, each sponsor of such child, and each adult member of the household of such sponsor, and in the case of a sponsor who asserts that they are a biological parent or biological relative of an unaccompanied alien child, confirm such relationship using DNA testing.\n**(5)**\nImmediately take custody of any unaccompanied alien child the Secretary has reason to believe may be subject to exploitation, abuse, or subject to unsafe conditions, and notify the Secretary of Homeland Security.\n**(6)**\nConduct home visits as follows:\n**(A)**\nVisit and inspect the household in which each unaccompanied alien child is proposed to be placed before such child may be released from the custody of the Secretary.\n**(B)**\nConduct not fewer than 6 unannounced, in-person visits during the first year of a placement of an unaccompanied alien child, and not fewer than 4 unannounced, in-person visits per year thereafter.\n##### (d) Vetting of sponsors\n**(1) Initial vetting**\nBefore releasing an unaccompanied alien child from the custody of the Secretary into the custody of a sponsor, the Secretary shall require such sponsor, and any adult member of the household of such sponsor, to provide the Secretary with their biometric information, and in consultation with the Attorney General, conduct a background check and vetting process that includes\u2014\n**(A)**\nan in-person interview and inspection;\n**(B)**\na public records check;\n**(C)**\na check of the Combined DNA Index System;\n**(D)**\na Federal Bureau of Investigation National Criminal History check;\n**(E)**\nan interagency check through the National Vetting Center;\n**(F)**\na check of the National Counterterrorism Center and Terrorism Screening Center;\n**(G)**\na child abuse and neglect check in relevant States;\n**(H)**\na check of the criminal history repository of the relevant States, localities, and any foreign country in which the sponsor has resided (to the greatest extent possible);\n**(I)**\na check of all Department of Homeland Security databases, to include a determination of immigration status;\n**(J)**\na check of the National Sex Offender Registry; and\n**(K)**\na synthetic identity check against fraudulent identities.\n**(2) Supplementary background checks**\nAfter placing an unaccompanied alien child into the custody of a sponsor, the Secretary shall, on an ongoing basis, and not less frequently than quarterly, conduct supplementary background checks and vetting to ensure that the sponsor and any adult member of the household of such sponsor continue to be eligible to have custody of the unaccompanied alien child.\n##### (e) Sponsor eligibility\nThe Secretary of Health and Human Services may not release an unaccompanied alien child to the custody of a sponsor, if such sponsor, or an adult member of the household of such sponsor\u2014\n**(1)**\nis an alien unlawfully present in the United States, unless such alien is the parent, legal guardian, or a biological relative of such unaccompanied alien child;\n**(2)**\nis an associate or member of\u2014\n**(A)**\na transnational criminal organization;\n**(B)**\na criminal street gang;\n**(C)**\nan enterprise involved in a pattern of racketeering activity or through the collection of an unlawful debt;\n**(D)**\na foreign terrorist organization, designated pursuant to section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); or\n**(E)**\nan entity designated as Specially Designated Global Terrorist, pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1702 );\n**(3)**\nis a sex offender who is required to register on the National Sex Offender Registry under section 113 of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20913 );\n**(4)**\nhas been convicted of crime under the laws of the United States, a State, or a political subdivision of a State, which\u2014\n**(A)**\ncarries a maximum sentence of 1 year or greater; or\n**(B)**\ncarries a maximum sentence of less than 1 year, during the 10-year period preceding the custody determination made by the Secretary;\n**(5)**\nhas been convicted of a crime of violence under the laws a foreign country; or\n**(6)**\nhas been charged with a crime under the laws of the United States, a State, or a political subdivision of a State, with respect to which the disposition is pending.\n##### (f) Failure To comply with conditions of release\n**(1) In general**\nIf, at any time, a sponsor fails to ensure that an unaccompanied alien child in the custody of the sponsor complies with the conditions of their release from the custody of the Secretary or the conditions of the Program, the Secretary shall\u2014\n**(A)**\nterminate the placement of the unaccompanied alien child with such sponsor;\n**(B)**\ntake custody of the unaccompanied alien child; and\n**(C)**\nprohibit such sponsor from sponsoring that unaccompanied alien child or any other unaccompanied alien child.\n**(2) Failure to comply**\nIn this subsection, failure to comply with the conditions of release includes failing to attend a court proceeding and violating an order of an immigration judge.\n##### (g) Definitions\nIn this Act:\n**(1)**\nThe term adult means an individual who is 18 years of age or older.\n**(2)**\nThe terms alien and immigration laws have the meanings given such terms in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ).\n**(3)**\nThe term continuously monitored by GPS means uninterrupted tracking of a person\u2019s location and movement history using satellite technology through a body worn device.\n**(4)**\nThe term crime of violence has the meaning given such term in section 16(a) of title 18, United States Code.\n**(5)**\nThe term criminal street gang has the meaning given such term in section 521(a) of title 18, United States Code.\n**(6)**\nThe terms enterprise , racketeering activity , pattern of racketeering activity , and unlawful debt have the meanings given to such terms in 1961 of title 18, United States Code.\n**(7)**\nThe term member of the household means, with respect to any person, any individual sharing a common abode as part of a single family unit with the person, including a domestic employee.\n**(8)**\nThe term telephonic reporting means a telephone call that compares the voice of the person calling to a biometric voiceprint of the person required to place such call.\n**(9)**\nThe term transnational criminal organization has the meaning given such term in section 3003 of the FEND Off Fentanyl Act ( 21 U.S.C. 2341 ).\n**(10)**\nThe term unaccompanied alien child has the meaning given such term in section 462(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g) ).",
      "versionDate": "2025-09-11",
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
        "name": "Immigration",
        "updateDate": "2025-09-24T15:02:57Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5324ih.xml"
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
      "title": "No More Missing Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No More Missing Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Unaccompanied Alien Child Anti-Trafficking Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:33:31Z"
    }
  ]
}
```
