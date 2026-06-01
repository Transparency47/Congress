# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2226
- Title: Necessary Environmental Exemptions for Defense Act
- Congress: 119
- Bill type: S
- Bill number: 2226
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2025-09-04T15:25:36Z
- Update date including text: 2025-09-04T15:25:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2226",
    "number": "2226",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Necessary Environmental Exemptions for Defense Act",
    "type": "S",
    "updateDate": "2025-09-04T15:25:36Z",
    "updateDateIncludingText": "2025-09-04T15:25:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-09",
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
          "date": "2025-07-09T19:22:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2226is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2226\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo exempt the Department of Defense from certain environmental protection activities.\n#### 1. Short title\nThis Act may be cited as the Necessary Environmental Exemptions for Defense Act .\n#### 2. Exemption of activities of Department of Defense from certain environmental protection laws\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Department of Defense (in this section referred to as the Department ) must operate with maximum agility and efficiency to ensure it is prepared to deter and, if necessary, fight and win a conflict with the Chinese Communist Party;\n**(2)**\nthe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1361 et seq. ), and the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ) frequently and unnecessarily delay the readiness and operations of the Armed Forces without substantial benefit to the environment or protected species; and\n**(3)**\nnational defense takes precedence over all administrative processes that might otherwise hinder the timely execution of defense-related activities.\n##### (b) Exemption\nThe Department and any component, contractor, or designee of the Department shall be exempt from any requirement under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1361 et seq. ), and the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ) for all activities, operations, permits, and projects conducted for the following purposes, if the President or the Secretary of Defense (in this section referred to as the Secretary ) certifies the activity is directly related to countering the threat of the Chinese Communist Party to the United States:\n**(1)**\nReadiness, training, or operations of the Armed Forces.\n**(2)**\nConstruction, maintenance, expansion, or repair of facilities or infrastructure of the Department.\n**(3)**\nDeployment, development, testing, or production of technologies, systems, or equipment of the Department.\n**(4)**\nDeployment, development, testing, or production of commercial technologies, systems, or equipment related to an agreement, grant, or contract with the Department, the timely completion of which directly contributes to a critical national security interest of the United States.\n##### (c) No alternative compliance obligations\nExcept for any environmental mitigations the Secretary may determine are appropriate\u2014\n**(1)**\nno Federal, State, or local environmental review process may be required as a substitute or replacement for compliance with the provisions of law exempted under subsection (b); and\n**(2)**\nno Federal, State, or local authority may require environmental evaluations for activities, operations, permits, or projects for which similar evaluations are exempted under subsection (b).\n##### (d) Review of environmental best practices\nNot later than 5 years after the date of the enactment of this Act, and not less frequently than every 5 years thereafter, the Secretary shall review best practices for environmental mitigations and update the policy of the Department as necessary to reflect changes in priorities of the Department and advancements in environmental practices.\n##### (e) Judicial preclusion\nNo court shall have jurisdiction to review, enjoin, or otherwise restrain any designation, activity, operation, permit, or project certification carried out or any determination made by the Department that is covered under subsection (b).\n##### (f) Retroactive application\nThis section shall apply to any activity, operation, or project described in subsection (b) that is ongoing as of the date of the enactment of this Act and shall nullify any legal action or administrative proceeding pending as of such date relating to compliance with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1361 et seq. ), or the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ) in connection with such activity, operation, or project.",
      "versionDate": "2025-07-09",
      "versionType": "Introduced in Senate"
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-04T15:25:36Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2226is.xml"
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
      "title": "Necessary Environmental Exemptions for Defense Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Necessary Environmental Exemptions for Defense Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to exempt the Department of Defense from certain environmental protection activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:31Z"
    }
  ]
}
```
