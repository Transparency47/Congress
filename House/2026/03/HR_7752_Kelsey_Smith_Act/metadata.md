# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7752?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7752
- Title: Kelsey Smith Act
- Congress: 119
- Bill type: HR
- Bill number: 7752
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-03-19T15:27:50Z
- Update date including text: 2026-03-19T15:27:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-02: Introduced in House

## Actions

- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7752",
    "number": "7752",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001228",
        "district": "2",
        "firstName": "Derek",
        "fullName": "Rep. Schmidt, Derek [R-KS-2]",
        "lastName": "Schmidt",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Kelsey Smith Act",
    "type": "HR",
    "updateDate": "2026-03-19T15:27:50Z",
    "updateDateIncludingText": "2026-03-19T15:27:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:00:35Z",
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
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "KS"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "KS"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7752ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7752\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Mr. Schmidt (for himself, Ms. Davids of Kansas , Mr. Estes , and Mr. Mann ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 2703 of title 18, United States Code, to require emergency disclosure of location information to law enforcement or public safety answering point.\n#### 1. Short title\nThis Act may be cited as the Kelsey Smith Act .\n#### 2. Required emergency disclosure of location information to law enforcement or public safety answering point\n##### (a) Definitions\nSection 2510 of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (20), by striking and at the end;\n**(2)**\nin paragraph (21), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(22) the term location information \u2014 (A) means any data or information concerning the current or most recently known location of a telecommunications device that, in whole or in part, is generated, derived from, or obtained by the operation of the device; and (B) does not include the contents of any wire or electronic communication; (23) the term telecommunications device means any customer premises equipment (as such term is defined in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 )); and (24) the term public safety answering point shall have the meaning given such term in section 7 of the Wireless Communications and Public Safety Act of 1999 ( 47 U.S.C. 615b ). .\n##### (b) Required emergency disclosure of location information to law enforcement or public safety answering point\nSection 2703 of title 18, United States Code, is amended by adding at the end the following:\n(i) (1) Location information requests At the request of an investigative or law enforcement officer, or an employee or other agent of a public safety answering point acting on behalf of such an officer, who is acting in the course of the official duties of such officer, a provider of electronic communication service shall provide to such officer the available location information of a telecommunications device without delay if the officer asserts\u2014 (A) (i) that the telecommunications device was used to contact a public safety answering point requesting emergency assistance during the preceding 48-hour period; or (ii) that the officer has reasonable suspicion that the telecommunications device is in the possession or presence of an individual who is involved in an emergency situation that involves the risk of death or serious physical harm; and (B) (i) the subscriber or customer of such electronic telecommunication service has consented to such request or, if such subscriber or customer is not reasonably available, then the next of kin of such subscriber or customer has consented; or (ii) (I) reasonable efforts have been made to obtain such consent or the consent of next of kin of such subscriber or customer; (II) such consent was neither obtained nor refused; and (III) such officer reasonably believes delay in providing the available location information may increase the risk of death or serious physical harm. (2) Records of disclosed records If an investigative or law enforcement officer, or an employee or other agent of a public safety answering point acting on behalf of such an officer, submits a request for location information to a provider of an electronic communication service under paragraph (1) the investigative or law enforcement agency employing the officer shall maintain a record of the request that includes each of the following: (A) The name of the officer or agent making the request (and, in the case of a request made by an agent, the name of the officer on whose behalf the agent is acting). (B) A declaration that disclosure of location information is needed based on the conditions described in clause (i) or (ii) of subparagraph (1)(A) and that the requirements of clause (i) or (ii) of subparagraph (1)(B) have been satisfied. (C) A description\u2014 (i) of the request that explains the need for disclosure of location information; and (ii) of the manner and the name of the person by whom the consent required by clause (i) of subparagraph (1)(B) was given or of the reasonable efforts required by clause (ii) of subparagraph (1)(B). (3) Relationship to State law (A) In general Nothing in this subsection shall exempt a telecommunications carrier or a provider of electronic communication service from complying with any applicable State law that requires the carrier or provider to provide location information of a telecommunications device to an investigative or law enforcement officer or an employee or other agent of a public safety answering point acting on behalf of such an officer in response to a request by such officer or agent. (B) Applicability A circumstance described in this subparagraph is a circumstance in which the officer or agent\u2014 (i) makes the request while acting in the course of the official duties of the officer or agent; and (ii) asserts that the request is made for the purpose of responding to\u2014 (I) a call for emergency services; or (II) an emergency situation that involves the risk of death or serious physical harm. (4) Next of kin determination For the purposes of this subsection, a next of kin determination shall be made in the following priority order: (A) Legal spouse. (B) Child (whether by current or prior marriage) age 18 years or older in descending precedence by age. (C) Father or mother, unless by court order custody has been vested in another (adoptive parent takes precedence over natural parent). (D) Sibling (whole or half) age 18 years or older in descending precedence by age. (E) Grandfather or grandmother. (F) Any other relative (precedence to be determined in accordance with the civil law of descent in the State in which the investigative or law enforcement officer is employed). .",
      "versionDate": "2026-03-02",
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
        "updateDate": "2026-03-19T15:27:50Z"
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
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7752ih.xml"
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
      "title": "Kelsey Smith Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kelsey Smith Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 2703 of title 18, United States Code, to require emergency disclosure of location information to law enforcement or public safety answering point.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T04:48:31Z"
    }
  ]
}
```
