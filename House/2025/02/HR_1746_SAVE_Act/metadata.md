# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1746?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1746
- Title: SAVE Act
- Congress: 119
- Bill type: HR
- Bill number: 1746
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-04-08T08:05:27Z
- Update date including text: 2025-04-08T08:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1746",
    "number": "1746",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "SAVE Act",
    "type": "HR",
    "updateDate": "2025-04-08T08:05:27Z",
    "updateDateIncludingText": "2025-04-08T08:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:09:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T18:01:25Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1746ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1746\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Stanton (for himself and Mr. Hamadeh of Arizona ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to the laws relating to the recognition of agents, attorneys, organizations and their representatives, and other individuals for the purposes of assisting in the preparation, presentation, and prosecution of claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Standardizing Accreditation information for Veteran Ease Act or the SAVE Act .\n#### 2. Annual report\n##### (a) In general\nChapter 59 of title 38, United States Code, is amended by adding at the end the following new sections:\n5907. Annual submission of information on recognition of agents, attorneys, organizations and their representatives, and other individuals The Secretary shall include in the annual report required to be submitted to Congress under section 529 of this title information on agents, attorneys, organizations and their representatives, and any other individuals recognized under this chapter. Such information shall include, for the year covered by the report, the following: (1) A description of the type and frequency of training that is required to be recognized, or to continue to be recognized, under this chapter and of any review or audit conducted of such training. (2) A description of the type of information the Secretary collects from individuals who request to be recognized, or to continue to be recognized, under this chapter. (3) A description of the method the Secretary uses to gather personal and qualifying information from individuals and organizations recognized or seeking recognition under this chapter. (4) An identification of the frequency with which the Secretary receives updated personal and qualifying information from individuals and organizations recognized under this chapter. (5) A description of the method the Secretary uses to verify personal and qualifying information received from individuals and organizations recognized or seeking recognition under this chapter. (6) An identification of the frequency with which individuals and organizations recognized under this chapter are required to comply with ongoing reporting requirements. (7) An identification of the number of Department employees responsible for the administration of this chapter. (8) An identification of the frequency with which the VA Accreditation Search database, or any successor to such database, is\u2014 (A) updated; and (B) checked for accuracy, including with respect to the accuracy of contact information and the removal of individuals and organizations no longer recognized to assist veterans in the preparation, presentation, or prosecution of claims under laws administered by the Secretary. (9) A description of the steps the Secretary has taken to ensure such database is updated. (10) An identification of any additional resources the Department may need to ensure that\u2014 (A) any published information regarding individuals and organizations recognized under this chapter is accurate and up-to date; and (B) individuals who are recognized under this chapter are of good moral character and in good repute, are qualified to render claimants valuable service, and are otherwise competent to assist claimants in presenting claims under laws administered by the Secretary. (11) An identification of the costs of processing applications for recognition under this chapter. (12) A description of the timeline for processing applications for recognition under this chapter. (13) An identification of how frequently individuals seeking recognition under this chapter are denied such recognition and for what reasons. (14) An identification of how frequently recognition is rescinded from individuals recognized under this chapter and for what reasons. 5908. Certification mark for identification of recognized individuals (a) In general The Secretary of Veterans Affairs shall establish and maintain a certification mark, which may be used to identify individuals who are recognized under this chapter for the purposes of assisting in the preparation, presentation, and prosecution of claims for benefits under the laws administered by the Secretary. Such certification mark shall be registered with the United States Patent and Trademark Office. (b) Civil penalty for violation (1) A person who displays or otherwise uses the certification mark established under subsection (a) for the fraudulent purpose of inducing the belief that the person is recognized under this chapter for the purposes of assisting in the preparation, presentation, and prosecution of claims for benefits under the laws administered by the Secretary shall be fined in accordance with title 18, imprisoned, or both. (2) This subsection shall not make unlawful the use of any such emblem, sign, insignia or words which was lawful on the date of enactment of this section. (3) Amounts collected as civil penalties pursuant to this subsection shall remain available for the Department of Veterans Affairs, without fiscal year limitation, for the purpose of enforcing paragraph (1). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 5906 the following new items:\n5907. Annual submission of information on recognition of agents, attorneys, organizations and their representatives, and other individuals. 5908. Certification mark for identification of recognized individuals. .\n#### 3. Biannual database accuracy\nNot later than 180 days after the date on which the Secretary submits the first report under section 529 of title 38, United States Code, that includes the information required to be submitted under section 5907 of title 38, United States Code, as added by section 2, and annually thereafter, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nprovide to each individual recognized under chapter 59 of title 38, United States Code, a notice that includes a request to update the contact information of the individual provided to the Department of Veterans Affairs;\n**(2)**\nmake publicly available instructions such individuals may use to update such contact information; and\n**(3)**\nensure the VA Accreditation Search Database is updated to include updated contact information.",
      "versionDate": "2025-02-27",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:08:07Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1746ih.xml"
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
      "title": "SAVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Standardizing Accreditation information for Veteran Ease Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements to the laws relating to the recognition of agents, attorneys, organizations and their representatives, and other individuals for the purposes of assisting in the preparation, presentation, and prosecution of claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:09Z"
    }
  ]
}
```
