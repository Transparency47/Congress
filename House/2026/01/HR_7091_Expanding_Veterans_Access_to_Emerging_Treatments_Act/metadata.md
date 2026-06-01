# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7091?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7091
- Title: Expanding Veterans’ Access to Emerging Treatments Act
- Congress: 119
- Bill type: HR
- Bill number: 7091
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-25T09:06:31Z
- Update date including text: 2026-02-25T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-02 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-02 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7091",
    "number": "7091",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Expanding Veterans\u2019 Access to Emerging Treatments Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:31Z",
    "updateDateIncludingText": "2026-02-25T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:41:32Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7091ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7091\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Bergman (for himself and Mr. Correa ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish an investigational research and extended access treatment program utilizing innovative treatments and emerging therapies to address conditions with unmet medical needs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Veterans\u2019 Access to Emerging Treatments Act .\n#### 2. Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nMany conditions, such as chronic pain, post-traumatic stress disorder, and substance use disorders, continue to challenge the veteran community amid a lack of new innovative treatments and emerging therapies.\n**(2)**\nThese and other conditions represent an urgent unmet medical need among veterans.\n**(3)**\nThe Department of Veterans Affairs should continue to advance research and facilitate timely access to innovative treatments and emerging therapies, including psychedelic- and entactogenic-assisted therapies, for veterans with such unmet treatment needs.\n#### 3. Research program of the Department of Veterans Affairs on innovative treatments and emerging therapies for certain covered conditions\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Secretary of Veterans Affairs shall develop an investigational research program for the treatment of veterans diagnosed with a covered condition using innovative treatments and emerging therapies, consistent with applicable Federal law, including laws governing investigational medical products and controlled substances. Not later than 60 days after the date of the enactment of this Act, the Secretary shall designate a lead administrator to carry out the research and treatment program under this section.\n##### (b) Investigational research program\nThe Department of Veterans Affairs may\u2014\n**(1)**\nconduct one or more clinical trials for the treatment of a covered condition that include veterans as participants in the clinical trial using innovative treatments and emerging therapies, which may be selected following a review of their efficacy, safety, and ease of administration; and\n**(2)**\ndevelop a compassionate or extended access protocol that facilitates consideration of, and as appropriate access to, innovative treatments and emerging therapies.\n##### (c) Participation in clinical trials or extended access\nThe Secretary shall establish a process under which a veteran diagnosed with a covered condition may\u2014\n**(1)**\nparticipate in a clinical trial conducted under this section; or\n**(2)**\nbe considered for access to an innovative treatment or emerging therapy under a compassionate or extended access protocol, as clinically appropriate.\n##### (d) Additional authority\nIn addition to carrying out the activities under this section, the Secretary may, using amounts otherwise authorized to be appropriated and otherwise available to the Department of Veterans Affairs, support one or more clinical research trials using innovative treatments and emerging therapies described in subsection (g).\n##### (e) Report required\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report, including the following:\n**(1)**\nIdentification of clinics designated to host activities under such a protocol under this section and the number of veterans expected to participate in a clinical trial conducted in subsection (b);\n**(2)**\nInformation on the findings and outcomes of such clinical trials, including preliminary outcomes; and\n**(3)**\nA review of all innovative treatments and emerging therapies utilized for the treatment of covered conditions, including safety and efficacy studies, cost, regulatory, and logistical considerations associated with each.\n##### (f) Sunset\nNot later than two years after the date of enactment of this Act, the investigational program shall be reviewed by the Secretary of Veterans Affairs, who may then choose to extend or terminate the program at their discretion.\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term innovative treatment means any of the following:\n**(A)**\n3,4-Methylenedioxy-methamphetamine;\n**(B)**\n5-Methoxy-N,N-dimethyltryptamine;\n**(C)**\n5-Methoxy-2-aminoindane;\n**(D)**\nIbogaine;\n**(E)**\nKetamine;\n**(F)**\nPsilocybin; and\n**(G)**\nSuch other treatments as may be designated by the Secretary.\n**(2)**\nThe term emerging therapies means any of the following:\n**(A)**\nInvestigational pharmaceutical candidates that meet the Government\u2019s Definition of Recovery;\n**(B)**\nInvestigational medical devices, such as deep brain neurostimulation or hyperbaric oxygen therapy; and\n**(C)**\nSuch other therapeutic interventions as may be designated by the Secretary.\n**(3)**\nThe term covered condition means any of the following:\n**(A)**\nAnxiety;\n**(B)**\nChronic pain;\n**(C)**\nDepression;\n**(D)**\nPost-traumatic stress disorder;\n**(E)**\nSubstance use disorders, including but not limited to alcohol use and cocaine use disorders;\n**(F)**\nTraumatic brain injury; and\n**(G)**\nSuch other conditions as may be designated by the Secretary.\n##### (h) Rule of construction\nNothing in this section shall be construed to require or direct the Secretary to act in a manner inconsistent with applicable Federal law, including laws governing investigational medical products and controlled substances.",
      "versionDate": "2026-01-15",
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
        "updateDate": "2026-02-03T17:27:50Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7091ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish an investigational research and extended access treatment program utilizing innovative treatments and emerging therapies to address conditions with unmet medical needs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-28T06:32:24Z"
    },
    {
      "title": "Expanding Veterans\u2019 Access to Emerging Treatments Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Veterans\u2019 Access to Emerging Treatments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-28T04:53:19Z"
    }
  ]
}
```
