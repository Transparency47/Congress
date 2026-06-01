# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1777?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1777
- Title: SECURE Notarization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1777
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-04-01T19:52:34Z
- Update date including text: 2026-04-01T19:52:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1777",
    "number": "1777",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B000668",
        "district": "2",
        "firstName": "Cliff",
        "fullName": "Rep. Bentz, Cliff [R-OR-2]",
        "lastName": "Bentz",
        "party": "R",
        "state": "OR"
      }
    ],
    "title": "SECURE Notarization Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-01T19:52:34Z",
    "updateDateIncludingText": "2026-04-01T19:52:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-03T17:07:20Z",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "ND"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CO"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TN"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1777ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1777\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Bentz (for himself, Ms. Dean of Pennsylvania , and Ms. Fedorchak ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize notaries public to perform, and to establish minimum standards for, electronic notarizations and remote notarizations that occur in or affect interstate commerce, to require any Federal court to recognize notarizations performed by a notarial officer of any State, to require any State to recognize notarizations performed by a notarial officer of any other State when the notarization was performed under or relates to a public Act, record, or judicial proceeding of the notarial officer\u2019s State or when the notarization occurs in or affects interstate commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing and Enabling Commerce Using Remote and Electronic Notarization Act of 2025 or the SECURE Notarization Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Communication technology**\nThe term communication technology , with respect to a notarization, means an electronic device or process that allows the notary public performing the notarization, a remotely located individual, and (if applicable) a credible witness to communicate with each other simultaneously by sight and sound during the notarization.\n**(2) Electronic; electronic record; electronic signature; information; person; record**\nThe terms electronic , electronic record , electronic signature , information , person , and record have the meanings given those terms in section 106 of the Electronic Signatures in Global and National Commerce Act ( 15 U.S.C. 7006 ).\n**(3) Law**\nThe term law includes any statute, regulation, rule, or rule of law.\n**(4) Notarial officer**\nThe term notarial officer means\u2014\n**(A)**\na notary public; or\n**(B)**\nany other individual authorized to perform a notarization under the laws of a State without a commission or appointment as a notary public.\n**(5) Notarial officer\u2019s State; notary public\u2019s State**\nThe term notarial officer\u2019s State or notary public\u2019s State means the State in which a notarial officer, or a notary public, as applicable, is authorized to perform a notarization.\n**(6) Notarization**\nThe term notarization \u2014\n**(A)**\nmeans any act that a notarial officer may perform under\u2014\n**(i)**\nFederal law, including this Act; or\n**(ii)**\nthe laws of the notarial officer's State; and\n**(B)**\nincludes any act described in subparagraph (A) and performed by a notarial officer\u2014\n**(i)**\nwith respect to\u2014\n**(I)**\na tangible record; or\n**(II)**\nan electronic record; and\n**(ii)**\nfor\u2014\n**(I)**\nan individual in the physical presence of the notarial officer; or\n**(II)**\na remotely located individual.\n**(7) Notary public**\nThe term notary public means an individual commissioned or appointed as a notary public to perform a notarization under the laws of a State.\n**(8) Personal knowledge**\nThe term personal knowledge , with respect to the identity of an individual, means knowledge of the identity of the individual through dealings sufficient to provide reasonable certainty that the individual has the identity claimed.\n**(9) Remotely located individual**\nThe term remotely located individual , with respect to a notarization, means an individual who is not in the physical presence of the notarial officer performing the notarization.\n**(10) Requirement**\nThe term requirement includes a duty, a standard of care, and a prohibition.\n**(11) Signature**\nThe term signature means\u2014\n**(A)**\nan electronic signature; or\n**(B)**\na tangible symbol executed or adopted by a person and evidencing the present intent to authenticate or adopt a record.\n**(12) Simultaneously**\nThe term simultaneously , with respect to a communication between parties\u2014\n**(A)**\nmeans that each party communicates substantially simultaneously and without unreasonable interruption or disconnection; and\n**(B)**\nincludes any reasonably short delay that is inherent in, or common with respect to, the method used for the communication.\n**(13) State**\nThe term State \u2014\n**(A)**\nmeans\u2014\n**(i)**\nany State of the United States;\n**(ii)**\nthe District of Columbia;\n**(iii)**\nthe Commonwealth of Puerto Rico;\n**(iv)**\nany territory or possession of the United States; and\n**(v)**\nany federally recognized Indian Tribe; and\n**(B)**\nincludes any executive, legislative, or judicial agency, court, department, board, office, clerk, recorder, register, registrar, commission, authority, institution, instrumentality, county, municipality, or other political subdivision of an entity described in any of clauses (i) through (v) of subparagraph (A).\n#### 3. Authorization to perform and minimum standards for electronic notarization\n##### (a) Authorization\nUnless prohibited under section 10, and subject to subsection (b), a notary public may perform a notarization that occurs in or affects interstate commerce with respect to an electronic record.\n##### (b) Requirements of electronic notarization\nIf a notary public performs a notarization under subsection (a), the following requirements shall apply with respect to the notarization:\n**(1)**\nThe electronic signature of the notary public, and all other information required to be included under other applicable law, shall be attached to or logically associated with the electronic record.\n**(2)**\nThe electronic signature and other information described in paragraph (1) shall be bound to the electronic record in a manner that renders any subsequent change or modification to the electronic record evident.\n#### 4. Authorization to perform and minimum standards for remote notarization\n##### (a) Authorization\nUnless prohibited under section 10, and subject to subsection (b), a notary public may perform a notarization that occurs in or affects interstate commerce for a remotely located individual.\n##### (b) Requirements of remote notarization\nIf a notary public performs a notarization under subsection (a), the following requirements shall apply with respect to the notarization:\n**(1)**\nThe remotely located individual shall appear personally before the notary public at the time of the notarization by using communication technology.\n**(2)**\nThe notary public shall\u2014\n**(A)**\nreasonably identify the remotely located individual\u2014\n**(i)**\nthrough personal knowledge of the identity of the remotely located individual; or\n**(ii)**\nby obtaining satisfactory evidence of the identity of the remotely located individual by\u2014\n**(I)**\nusing not fewer than 2 distinct types of processes or services through which a third person provides a means to verify the identity of the remotely located individual through a review of public or private data sources; or\n**(II)**\noath or affirmation of a credible witness who\u2014\n**(aa)**\n(AA)\nis in the physical presence of the notary public or the remotely located individual; or\n(BB)\nappears personally before the notary public and the remotely located individual by using communication technology;\n**(bb)**\nhas personal knowledge of the identity of the remotely located individual; and\n**(cc)**\nhas been identified by the notary public in the same manner as specified for identification of a remotely located individual under clause (i) or subclause (I) of this clause;\n**(B)**\neither directly or through an agent\u2014\n**(i)**\ncreate an audio and visual recording of the performance of the notarization; and\n**(ii)**\nnotwithstanding any resignation from, or revocation, suspension, or termination of, the notary public\u2019s commission or appointment, retain the recording created under clause (i) as a notarial record\u2014\n**(I)**\nfor a period of not less than\u2014\n**(aa)**\nif an applicable law of the notary public\u2019s State specifies a period of retention, the greater of\u2014\n(AA)\nthat specified period; or\n(BB)\n5 years after the date on which the recording is created; or\n**(bb)**\nif no applicable law of the notary public\u2019s State specifies a period of retention, 10 years after the date on which the recording is created; and\n**(II)**\nif any applicable law of the notary public\u2019s State governs the content, manner or place of retention, security, use, effect, or disclosure of the recording or any information contained in the recording, in accordance with that law; and\n**(C)**\nif the notarization is performed with respect to a tangible or electronic record, take reasonable steps to confirm that the record before the notary public is the same record with respect to which the remotely located individual made a statement or on which the individual executed a signature.\n**(3)**\nIf a guardian, conservator, executor, personal representative, administrator, or similar fiduciary or successor is appointed for or on behalf of a notary public or a deceased notary public under applicable law, that person shall retain the recording under paragraph (2)(B)(ii), unless\u2014\n**(A)**\nanother person is obligated to retain the recording under applicable law of the notary public\u2019s State; or\n**(B)**\n**(i)**\nunder applicable law of the notary public\u2019s State, that person may transmit the recording to an office, archive, or repository approved or designated by the State; and\n**(ii)**\nthat person transmits the recording to the office, archive, or repository described in clause (i) in accordance with applicable law of the notary public\u2019s State.\n**(4)**\nIf the remotely located individual is physically located outside the geographic boundaries of a State, or is otherwise physically located in a location that is not subject to the jurisdiction of the United States, at the time of the notarization\u2014\n**(A)**\nthe record shall\u2014\n**(i)**\nbe intended for filing with, or relate to a matter before, a court, governmental entity, public official, or other entity that is subject to the jurisdiction of the United States; or\n**(ii)**\ninvolve property located in the territorial jurisdiction of the United States or a transaction substantially connected to the United States; and\n**(B)**\nthe act of making the statement or signing the record may not be prohibited by a law of the jurisdiction in which the individual is physically located.\n##### (c) Personal appearance satisfied\nIf a State or Federal law requires an individual to appear personally before or be in the physical presence of a notary public at the time of a notarization, that requirement shall be considered to be satisfied if\u2014\n**(1)**\nthe individual\u2014\n**(A)**\nis a remotely located individual; and\n**(B)**\nappears personally before the notary public at the time of the notarization by using communication technology; and\n**(2)**\n**(A)**\nthe notarization was performed under or relates to a public act, record, or judicial proceeding of the notary public\u2019s State; or\n**(B)**\nthe notarization occurs in or affects interstate commerce.\n#### 5. Recognition of notarizations in Federal court\n##### (a) Recognition of validity\nEach court of the United States shall recognize as valid under the State or Federal law applicable in a judicial proceeding before the court any notarization performed by a notarial officer of any State if the notarization is valid under the laws of the notarial officer\u2019s State or under this Act.\n##### (b) Legal effect of recognized notarization\nA notarization recognized under subsection (a) shall have the same effect under the State or Federal law applicable in the applicable judicial proceeding as if that notarization was validly performed\u2014\n**(1)**\n**(A)**\nby a notarial officer of the State, the law of which is applicable in the proceeding; or\n**(B)**\nunder this Act or other Federal law; and\n**(2)**\nwithout regard to whether the notarization was performed\u2014\n**(A)**\nwith respect to\u2014\n**(i)**\na tangible record; or\n**(ii)**\nan electronic record; or\n**(B)**\nfor\u2014\n**(i)**\nan individual in the physical presence of the notarial officer; or\n**(ii)**\na remotely located individual.\n##### (c) Presumption of genuineness\nIn a determination of the validity of a notarization for the purposes of subsection (a), the signature and title of an individual performing the notarization shall be prima facie evidence in any court of the United States that the signature of the individual is genuine and that the individual holds the designated title.\n##### (d) Conclusive evidence of authority\nIn a determination of the validity of a notarization for the purposes of subsection (a), the signature and title of the following notarial officers of a State shall conclusively establish the authority of the officer to perform the notarization:\n**(1)**\nA notary public of that State.\n**(2)**\nA judge, clerk, or deputy clerk of a court of that State.\n#### 6. Recognition by State of notarizations performed under authority of another State\n##### (a) Recognition of validity\nEach State shall recognize as valid under the laws of that State any notarization performed by a notarial officer of any other State if\u2014\n**(1)**\nthe notarization is valid under the laws of the notarial officer\u2019s State or under this Act; and\n**(2)**\n**(A)**\nthe notarization was performed under or relates to a public act, record, or judicial proceeding of the notarial officer\u2019s State; or\n**(B)**\nthe notarization occurs in or affects interstate commerce.\n##### (b) Legal effect of recognized notarization\nA notarization recognized under subsection (a) shall have the same effect under the laws of the recognizing State as if that notarization was validly performed by a notarial officer of the recognizing State, without regard to whether the notarization was performed\u2014\n**(1)**\nwith respect to\u2014\n**(A)**\na tangible record; or\n**(B)**\nan electronic record; or\n**(2)**\nfor\u2014\n**(A)**\nan individual in the physical presence of the notarial officer; or\n**(B)**\na remotely located individual.\n##### (c) Presumption of genuineness\nIn a determination of the validity of a notarization for the purposes of subsection (a), the signature and title of an individual performing a notarization shall be prima facie evidence in any State court or judicial proceeding that the signature is genuine and that the individual holds the designated title.\n##### (d) Conclusive evidence of authority\nIn a determination of the validity of a notarization for the purposes of subsection (a), the signature and title of the following notarial officers of a State shall conclusively establish the authority of the officer to perform the notarization:\n**(1)**\nA notary public of that State.\n**(2)**\nA judge, clerk, or deputy clerk of a court of that State.\n#### 7. Electronic and remote notarization not required\nNothing in this Act may be construed to require a notary public to perform a notarization\u2014\n**(1)**\nwith respect to an electronic record;\n**(2)**\nfor a remotely located individual; or\n**(3)**\nusing a technology that the notary public has not selected.\n#### 8. Validity of notarizations; rights of aggrieved persons not affected; State laws on the practice of law not affected\n##### (a) Validity not affected\nThe failure of a notary public to meet a requirement under section 3 or 4 in the performance of a notarization, or the failure of a notarization to conform to a requirement under section 3 or 4, shall not invalidate or impair the validity or recognition of the notarization.\n##### (b) Rights of aggrieved persons\nThe validity and recognition of a notarization under this Act may not be construed to prevent an aggrieved person from seeking to invalidate a record or transaction that is the subject of a notarization or from seeking other remedies based on State or Federal law other than this Act for any reason not specified in this Act, including on the basis\u2014\n**(1)**\nthat a person did not, with present intent to authenticate or adopt a record, execute a signature on the record;\n**(2)**\nthat an individual was incompetent, lacked authority or capacity to authenticate or adopt a record, or did not knowingly and voluntarily authenticate or adopt a record; or\n**(3)**\nof fraud, forgery, mistake, misrepresentation, impersonation, duress, undue influence, or other invalidating cause.\n##### (c) Rule of construction\nNothing in this Act may be construed to affect a State law governing, authorizing, or prohibiting the practice of law.\n#### 9. Exception to preemption\n##### (a) In general\nA State law may modify, limit, or supersede the provisions of section 3, or subsection (a) or (b) of section 4, with respect to State law only if that State law\u2014\n**(1)**\neither\u2014\n**(A)**\nconstitutes an enactment or adoption of the Revised Uniform Law on Notarial Acts, as approved and recommended for enactment in all the States by the National Conference of Commissioners on Uniform State Laws in 2018 or the Revised Uniform Law on Notarial Acts, as approved and recommended for enactment in all the States by the National Conference of Commissioners on Uniform State Laws in 2021, except that a modification to such Law enacted or adopted by a State shall be preempted to the extent such modification\u2014\n**(i)**\nis inconsistent with a provision of section 3 or subsection (a) or (b) of section 4, as applicable; or\n**(ii)**\nwould not be permitted under subparagraph (B); or\n**(B)**\nspecifies additional or alternative procedures or requirements for the performance of notarizations with respect to electronic records or for remotely located individuals, if those additional or alternative procedures or requirements\u2014\n**(i)**\nare consistent with section 3 and subsections (a) and (b) of section 4; and\n**(ii)**\ndo not accord greater legal effect to the implementation or application of a specific technology or technical specification for performing those notarizations; and\n**(2)**\nrequires the retention of an audio and visual recording of the performance of a notarization for a remotely located individual for a period of not less than 5 years after the recording is created.\n##### (b) Rule of construction\nNothing in section 5 or 6 may be construed to preclude the recognition of a notarization under applicable State law, regardless of whether such State law is consistent with section 5 or 6.\n#### 10. Standard of care; special notarial commissions; false advertising\n##### (a) State standards of care; authority of State regulatory officials\nNothing in this Act may be construed to prevent a State, or a notarial regulatory official of a State, from\u2014\n**(1)**\nadopting a requirement in this Act as a duty or standard of care under the laws of that State or sanctioning a notary public for breach of such a duty or standard of care;\n**(2)**\nestablishing requirements and qualifications for, or denying, refusing to renew, revoking, suspending, or imposing a condition on, a commission or appointment as a notary public;\n**(3)**\ncreating or designating a class or type of commission or appointment, or requiring an endorsement or other authorization to be received by a notary public, as a condition on the authority to perform notarizations with respect to electronic records or for remotely located individuals; or\n**(4)**\nprohibiting a notary public from performing a notarization under section 3 or 4 as a sanction for a breach of duty or standard of care or for official misconduct.\n##### (b) Special commissions or authorizations created by a State; sanction for breach or official misconduct; false advertising\nA notary public may not perform a notarization under section 3 or 4 if any of the following applies:\n**(1)**\nThe notary public\u2019s State has enacted a law that creates or designates a class or type of commission or appointment, or requires an endorsement or other authorization to be received by a notary public, as a condition on the authority to perform notarizations with respect to electronic records or for remotely located individuals, and\u2014\n**(A)**\nthe commission or appointment of the notary public is not of that class or type; or\n**(B)**\nthe notary public has not received the endorsement or other authorization.\n**(2)**\nThe notarial regulatory official of the notary public\u2019s State has prohibited the notary public from performing the notarization as a sanction for a breach of duty or standard of care or for official misconduct.\n**(3)**\n**(A)**\nThe notary public has engaged in false or deceptive advertising.\n**(B)**\nFor the purposes of subparagraph (A), a notary public shall be considered to have engaged in false or deceptive advertising if the notary public (unless the notary public is an attorney licensed to practice law in a State)\u2014\n**(i)**\nuses the term notario or notario publico ; or\n**(ii)**\nstates or represents in a record offering commercial notarial services that the notary public is authorized to\u2014\n**(I)**\nassist in drafting legal records, give legal advice, or otherwise practice law;\n**(II)**\nact as an immigration consultant or an expert on matters pertaining to immigration;\n**(III)**\nrepresent a person in a judicial or administrative proceeding relating to immigration to the United States, United States citizenship, or related matters; or\n**(IV)**\nreceive compensation for performing any activity described in this subparagraph.\n**(C)**\nFor the purposes of a notarization performed by a notary public under section 4 for a remotely located individual, if a record executed by the remotely located individual attests that the notary public disclosed to the individual the prohibitions under this paragraph, and that the notary public did not make any statement or representation in violation of this paragraph, that record shall conclusively establish compliance by the notary public with the requirements of this paragraph, as of the date on which the individual executes that record.\n#### 11. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be invalid or unconstitutional, the remainder of this Act and the application of the provisions thereof to other persons or circumstances shall not be affected by that holding.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1561",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SECURE Notarization Act of 2025",
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
            "name": "Computers and information technology",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2026-02-04T19:31:23Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-04T19:31:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-03-19T16:08:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1777",
          "measure-number": "1777",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1777v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing and Enabling Commerce Using Remote and Electronic Notarization Act of 2025 or the SECURE Notarization Act of 2025\u00a0</strong></p><p>This bill allows a notary public commissioned under state law to remotely notarize electronic records and perform notarizations for remotely located individuals. The bill provides technical requirements for the notarizations, including the creation and retention of video and audio recordings and the use of communication technologies (i.e., video chat).</p><p>Additionally, the bill requires U.S. courts and states to recognize notarizations\u2014including remote notarizations of electronic records and notarizations of remotely-located individuals\u2014that occur in or affect interstate commerce and are performed by a notary public commissioned under the laws of other states.</p><p>The bill also allows a notary public to remotely notarize electronic records involving an individual located outside of the United States, subject to certain requirements.</p>"
        },
        "title": "SECURE Notarization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1777.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing and Enabling Commerce Using Remote and Electronic Notarization Act of 2025 or the SECURE Notarization Act of 2025\u00a0</strong></p><p>This bill allows a notary public commissioned under state law to remotely notarize electronic records and perform notarizations for remotely located individuals. The bill provides technical requirements for the notarizations, including the creation and retention of video and audio recordings and the use of communication technologies (i.e., video chat).</p><p>Additionally, the bill requires U.S. courts and states to recognize notarizations\u2014including remote notarizations of electronic records and notarizations of remotely-located individuals\u2014that occur in or affect interstate commerce and are performed by a notary public commissioned under the laws of other states.</p><p>The bill also allows a notary public to remotely notarize electronic records involving an individual located outside of the United States, subject to certain requirements.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr1777"
    },
    "title": "SECURE Notarization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing and Enabling Commerce Using Remote and Electronic Notarization Act of 2025 or the SECURE Notarization Act of 2025\u00a0</strong></p><p>This bill allows a notary public commissioned under state law to remotely notarize electronic records and perform notarizations for remotely located individuals. The bill provides technical requirements for the notarizations, including the creation and retention of video and audio recordings and the use of communication technologies (i.e., video chat).</p><p>Additionally, the bill requires U.S. courts and states to recognize notarizations\u2014including remote notarizations of electronic records and notarizations of remotely-located individuals\u2014that occur in or affect interstate commerce and are performed by a notary public commissioned under the laws of other states.</p><p>The bill also allows a notary public to remotely notarize electronic records involving an individual located outside of the United States, subject to certain requirements.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr1777"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1777ih.xml"
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
      "title": "SECURE Notarization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SECURE Notarization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing and Enabling Commerce Using Remote and Electronic Notarization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize notaries public to perform, and to establish minimum standards for, electronic notarizations and remote notarizations that occur in or affect interstate commerce, to require any Federal court to recognize notarizations performed by a notarial officer of any State, to require any State to recognize notarizations performed by a notarial officer of any other State when the notarization was performed under or relates to a public Act, record, or judicial proceeding of the notarial officer's State or when the notarization occurs in or affects interstate commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:31Z"
    }
  ]
}
```
