# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7964?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7964
- Title: Halt Immigration from Countries with Inadequate Verification Capabilities Act
- Congress: 119
- Bill type: HR
- Bill number: 7964
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-04-03T22:20:13Z
- Update date including text: 2026-04-03T22:20:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7964",
    "number": "7964",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Halt Immigration from Countries with Inadequate Verification Capabilities Act",
    "type": "HR",
    "updateDate": "2026-04-03T22:20:13Z",
    "updateDateIncludingText": "2026-04-03T22:20:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T14:00:05Z",
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "TN"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7964ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7964\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Mr. Ogles (for himself, Mr. Fine , Mr. Donalds , and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to prohibit the admission of aliens from certain countries where the United States cannot reliably verify the identities or backgrounds of individuals seeking entry, building upon the framework established by Presidential Proclamation 9645 and upheld by the Supreme Court in Trump v. Hawaii, 585 U.S. (2018), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Halt Immigration from Countries with Inadequate Verification Capabilities Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Supreme Court, in Trump v. Hawaii, 585 U.S. (2018), upheld the President\u2019s authority to restrict entry from countries posing national security risks due to inadequate information-sharing and verification capabilities, affirming that such measures are within the executive\u2019s broad discretion under section 212(f) of the Immigration and Nationality Act and do not violate the Establishment Clause when facially neutral and justified by legitimate national security concerns.\n**(2)**\nPresidential Proclamation 9645 (issued September 24, 2017) identified countries with deficient identity-management practices, inadequate information-sharing on public-safety and terrorism threats, or other risk factors, including Iran, Libya, North Korea, Somalia, Syria, Venezuela, and Yemen, as warranting entry restrictions.\n**(3)**\nExpanding such restrictions to additional countries meeting similar criteria, such as those with ongoing instability, state-sponsored terrorism, or failure to cooperate in verification processes, is necessary to protect U.S. national security, consistent with the precedents set in Trump v. Hawaii and prior executive actions.\n**(4)**\nThis Act builds upon the upheld framework to include countries like Afghanistan, Sudan, Eritrea, and the Central African Republic, where reliable verification of individuals\u2019 identities and backgrounds is not feasible due to governance failures, conflict, or adversarial policies.\n#### 3. Definitions\nIn this Act:\n**(1)**\nThe term designated country means\u2014\n**(A)**\nSomalia;\n**(B)**\nany country identified in Presidential Proclamation 9645, as upheld in Trump v. Hawaii, including Iran, Libya, North Korea, Syria, Venezuela, and Yemen; and\n**(C)**\nany other country designated by the Secretary of State, in consultation with the Secretary of Homeland Security and the Director of National Intelligence, as a country where the government or prevailing conditions do not allow for reliable verification of the identities, backgrounds, or intentions of individuals seeking admission to the United States, based on factors such as inadequate information sharing, lack of diplomatic cooperation, state failure, or heightened national security risks, including but not limited to Afghanistan, Sudan, Eritrea, and the Central African Republic.\n**(2)**\nThe term alien has the meaning given such term in section 101(a)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(3) ).\n**(3)**\nThe term admission has the meaning given such term in section 101(a)(13) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(13) ).\n#### 4. Prohibition on admission of aliens from designated countries\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary of Homeland Security, in consultation with the Secretary of State and the Director of National Intelligence, shall prohibit the admission of any alien who is a national of, or who has resided in, a designated country during the 5-year period preceding the date of application for admission.\n##### (b) Exceptions\nThe prohibition under subsection (a) shall not apply to\u2014\n**(1)**\nan alien who is a lawful permanent resident of the United States;\n**(2)**\nan alien admitted as a refugee or granted asylum prior to the date of enactment of this Act;\n**(3)**\nan alien serving in the United States Armed Forces or any immediate family member of that alien;\n**(4)**\nan alien traveling on a diplomatic visa issued by that alien\u2019s country of origin; or\n**(5)**\nan alien whose admission is deemed by the Secretary of Homeland Security to be in the national interest, on a case-by-case basis, including students and certain nonimmigrant categories subject to enhanced screening as referenced in Presidential Proclamation 9645.\n##### (c) Waiver authority\nThe Secretary of Homeland Security may waive the application of subsection (a) for an alien if the Secretary determines that such waiver is necessary for humanitarian reasons or to ensure compliance with international obligations, consistent with the waiver processes upheld in Trump v. Hawaii.\n#### 5. Designation and review process\n##### (a) Initial designations\nNot later than 60 days after the date of enactment of this Act, the Secretary of State shall publish in the Federal Register a list of designated countries under section 3(1)(C), including the rationale for each designation, with reference to the verification standards outlined in Presidential Proclamation 9645 and the Supreme Court\u2019s decision in Trump v. Hawaii.\n##### (b) Annual review\nThe Secretary of State shall review the list of designated countries annually and may add or remove countries based on updated assessments of verification capabilities and national security risks, similar to the reviews conducted under prior executive orders. Any changes shall be published in the Federal Register with a 30-day notice period.\n##### (c) Congressional oversight\nThe Secretary of State shall submit to the appropriate congressional committees an annual report detailing the designations, including classified annexes as necessary.\n#### 6. Enhanced vetting procedures\n##### (a) Development\nThe Secretary of Homeland Security, in coordination with the Secretary of State, shall develop and implement enhanced vetting procedures for aliens from designated countries who may qualify for exceptions or waivers under section 4, drawing from the procedures established in Presidential Proclamation 9645.\n##### (b) Implementation timeline\nSuch procedures shall be implemented not later than 180 days after the date of enactment of this Act.\n#### 7. Enforcement and penalties\n##### (a) Enforcement\nThe provisions of this Act shall be enforced in accordance with the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n##### (b) Penalties\nAny alien who attempts to enter the United States in violation of this Act shall be subject to removal proceedings and barred from reentry for a period of 10 years.\n#### 8. Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held invalid, the remainder of this Act, and the application of such provision to other persons or circumstances, shall not be affected thereby.\n#### 9. Effective date\nThis Act shall take effect on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2026-03-17",
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
        "updateDate": "2026-04-03T22:20:13Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7964ih.xml"
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
      "title": "Halt Immigration from Countries with Inadequate Verification Capabilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Halt Immigration from Countries with Inadequate Verification Capabilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to prohibit the admission of aliens from certain countries where the United States cannot reliably verify the identities or backgrounds of individuals seeking entry, building upon the framework established by Presidential Proclamation 9645 and upheld by the Supreme Court in Trump v. Hawaii, 585 U.S. (2018), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:48:34Z"
    }
  ]
}
```
